from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Dados, Produtos, ItemPedido, Pedido, Acompanhamento, Proteina
from django.http import JsonResponse
from decimal import Decimal
import json

# Create your views here.
def index(request):
    dados = get_object_or_404(Dados, id=1)
    produtos = get_object_or_404(Produtos, id=1)
    quentinhas = Produtos.objects.filter(tipo='Q')
    bebidas = Produtos.objects.filter(tipo='B')
    dados_produto = {
        'dados': dados,
        'produtos': produtos,
        'quentinhas': quentinhas,
        'bebidas': bebidas}
    return render(request, "index.html", dados_produto)
def empresa(request):
    dados = get_object_or_404(Dados, id=1)
    return render(request, "empresa.html", {'dados': dados})
def contatos(request):
    dados = get_object_or_404(Dados, id=1)
    return render(request, "contatos.html", {'dados': dados})
def blog(request):
    dados = get_object_or_404(Dados, id=1)
    return render(request, "blog.html", {'dados': dados})
def cardapio(request):
    dados = get_object_or_404(Dados, id=1)
    produtos = get_object_or_404(Produtos, id=1)
    quentinhas = Produtos.objects.filter(tipo='Q' ,ativo=True)
    bebidas = Produtos.objects.filter(tipo='B')
    proteinas = Proteina.objects.filter(ativo=True)
    acompanhamento = Acompanhamento.objects.filter(ativo=True)
    dados_produto = {
        'dados': dados,
        'produtos': produtos,
        'quentinhas': quentinhas,
        'bebidas': bebidas,
        'acompanhamento': acompanhamento,
        'proteinas': proteinas
        }

    return render(request, "menu.html", dados_produto)

def produto_cardapio(request, id):
    produto = get_object_or_404(Produtos, id=id)
    dados = get_object_or_404(Dados, id=1)
    dados_produto = {
        'id':produto.id,
        'titulo': produto.titulo,
        'preco': str(produto.valor_promo),
        'tipo': produto.tipo,
        'capa': produto.capa,
        'acompanhamentos': Acompanhamento.objects.filter(ativo=True),
        'proteinas':  Proteina.objects.filter(ativo=True) 
    }
    context = {
        'dados_produto': dados_produto,
        'dados':dados
    }
    return render(request, "produto.html", context)


def produto_detalhes(request, id):
    produto = get_object_or_404(Produtos, id=id)
    
    dados_produto = {
        'titulo': produto.titulo,
        'descricao': produto.descricao,
        'preco': str(produto.valor_promo),
        'tipo': produto.tipo
    }
    return JsonResponse(dados_produto)




def carrinho(request):
    carrinho = request.session.get('carrinho', {})
    total_carrinho = 0

    for item_id, item in carrinho.items():
        item['total'] = item['preco'] * item['quantidade']
        total_carrinho += item['total']
    
    context = {
        'carrinho': carrinho,
        'total_carrinho': total_carrinho,
    }
    return render(request, 'ver_carrinho.html', context)

def atualizar_quantidade(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantidade = int(request.POST.get('quantidade'))

        # Obter o carrinho da sessão
        carrinho = request.session.get('carrinho', {})

        # Atualizar a quantidade do item
        if item_id in carrinho:
            carrinho[item_id]['quantidade'] = quantidade

        # Atualizar o carrinho na sessão
        request.session['carrinho'] = carrinho

        return redirect('ver_carrinho')

    return JsonResponse({'error': 'Método não permitido'}, status=405)

def remover_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')

        # Obter o carrinho da sessão
        carrinho = request.session.get('carrinho', {})

        # Remover o item do carrinho
        if item_id in carrinho:
            del carrinho[item_id]

        # Atualizar o carrinho na sessão
        request.session['carrinho'] = carrinho

        return redirect('ver_carrinho')

    return JsonResponse({'error': 'Método não permitido'}, status=405)




#Views não usadas no ate o momento

def finalizar_pedido(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        
        pedido = Pedido.objects.create(nome=nome, telefone=telefone)
        
        carrinho = request.session.get('carrinho', {})
        for produto_id, item in carrinho.items():
            produto = get_object_or_404(Produtos, id=produto_id)
            ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=item['quantidade'])
        
        # Lógica para enviar os detalhes do pedido para o WhatsApp
        pedido_detalhes = f'Pedido de {nome}:\nTelefone: {telefone}\n'
        for item in pedido.itens.all():
            pedido_detalhes += f'{item.quantidade} x {item.produto.titulo} - R${item.get_total()}\n'
        pedido_detalhes += f'Total do Pedido: R${sum(item.get_total() for item in pedido.itens.all())}'
        
        # Use a API do WhatsApp para enviar os detalhes do pedido
        # Aqui você pode usar uma biblioteca como Twilio para enviar mensagens para o WhatsApp
        
        # Limpar o carrinho após finalizar o pedido
        request.session['carrinho'] = {}
        
        return render(request, 'pedido_finalizado.html', {'pedido_detalhes': pedido_detalhes})
    
    return render(request, 'finalizar_pedido.html')

def adicionar_ao_carrinho(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        proteinas_ids = request.POST.getlist('proteinas')
        acompanhamentos_ids = request.POST.getlist('acompanhamentos')
        observacao = request.POST.get('observacao', '')

        # Obter o produto
        produto = get_object_or_404(Produtos, id=produto_id)

        # Obter proteinas e acompanhamentos
        proteinas = Proteina.objects.filter(id__in=proteinas_ids)
        acompanhamentos = Acompanhamento.objects.filter(id__in=acompanhamentos_ids)

        # Obter ou criar o carrinho na sessão
        carrinho = request.session.get('carrinho', {})

        # Criar um identificador único para o item no carrinho
        item_id = f'{produto_id}_{",".join(proteinas_ids)}_{",".join(acompanhamentos_ids)}'

        # Adicionar item ao carrinho
        if item_id not in carrinho:
            carrinho[item_id] = {
                'produto': produto.titulo,
                'imagem':produto.capa ,
                'preco': float(produto.valor_promo),  # converter Decimal para float
                'proteinas': [proteina.titulo for proteina in proteinas],
                'acompanhamentos': [acomp.nome for acomp in acompanhamentos],
                'observacao': observacao,
                'quantidade': 1
            }
        else:
            # Se já existir, apenas incrementar a quantidade
            carrinho[item_id]['quantidade'] += 1

        # Atualizar o carrinho na sessão
        request.session['carrinho'] = carrinho

        # Redirecionar para a página do menu
        return redirect('menu')  # Certifique-se de que a URL 'menu' está configurada corretamente

    return JsonResponse({'error': 'Método não permitido'}, status=405)
    

def cartTeste(request):
    carrinho = request.session.get('carrinho', {})
    total_carrinho = 0
    print(carrinho.items())
    for item_id, item in carrinho.items():
        item['total'] = item['preco'] * item['quantidade']
        total_carrinho += item['total']


    context = {
        'carrinho': carrinho,
        'total_carrinho': total_carrinho,
    }
    return render(request, 'ver_carrinho2.html', context)