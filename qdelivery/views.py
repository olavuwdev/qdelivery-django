from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Dados, Produtos, ItemPedido, Pedido, Acompanhamento, Proteina, Bairro
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import json

#importando funções

from .utils import *

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
    identificador = request.session.get('user_id')
    if not identificador:
        criar_identificador(request)
    else:
        print(f"Identificador já existente: {identificador}")

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
    identificador = request.session.get('user_id')
    if not identificador:
        criar_identificador(request)
    else:
        print(f"Identificador já existente: {identificador}")
    

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
    total_carrinho = func_total_carrinho(carrinho)


    
    context = {
        'carrinho': carrinho,
        'total_carrinho': total_carrinho,
    }
    return render(request, 'ver_carrinho.html', context)

""" 
    #Função atualizar antiga

    def atualizar_quantidade(request):
    if request.method == 'POST':
        # Decodifica o corpo da requisição JSON
        data = json.loads(request.body)
        item_id = data.get('item_id')
        quantidade = data.get('quantidade')

        # Obter o carrinho da sessão
        carrinho = request.session.get('carrinho', {})

        # Atualizar a quantidade do item
        if item_id in carrinho:
            carrinho[item_id]['quantidade'] = quantidade
            # Atualizar o total do item
            carrinho[item_id]['total'] = carrinho[item_id]['preco'] * quantidade

        # Atualizar o carrinho na sessão
        request.session['carrinho'] = carrinho
        request.session.modified = True  # Marca a sessão como modificada

        # Calcular o novo total do carrinho
        total_carrinho = sum(item['total'] for item in carrinho.values())

        return JsonResponse({'success': True, 'total_carrinho': total_carrinho})

    return JsonResponse({'error': 'Método não permitido'}, status=405) """



@require_POST
@csrf_exempt  # Necessário se o CSRF não for tratado no frontend (por segurança, ideal tratar no JS)
def atualizar_quantidade(request):
    data = json.loads(request.body)
    item_id = str(data.get('item_id'))
    nova_quantidade = data.get('quantidade')

    carrinho = request.session.get('carrinho', {})

    if item_id in carrinho:
        carrinho[item_id]['quantidade'] = nova_quantidade
        carrinho[item_id]['total'] = nova_quantidade * carrinho[item_id]['preco']
        request.session['carrinho'] = carrinho  # Salva a sessão
        return JsonResponse({'success': True, 'message': 'Quantidade atualizada com sucesso.'})
    else:
        return JsonResponse({'success': False, 'message': 'Item não encontrado no carrinho.'}, status=404)

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



from datetime import datetime
#Views não usadas no ate o momento

def finalizar_pedido(request):
    ##Get banco de dados

    bairro = Bairro.objects.all()

    carrinho = request.session.get('carrinho', {})
    #Valor total do carrinho
    total_carrinho = request.POST.get('total_carrinho')

    context = {
        'bairros': bairro,
        'total_carrinho': total_carrinho
        }
    if request.method == 'POST':
        usuario = request.session.get('usuario', {})
        usuario = {
            'nome': request.POST.get('nome', ''),
            'telefone': request.POST.get('telefone', '')
        }
        #Pedido.objects.create(nome=usuario['nome'], telefone=usuario['telefone'], endereco="Rua Teste")
        context['usuario'] = usuario
        print(f"{datetime.now()}  {usuario} carrinho: {carrinho} \n Total a pagar: {total_carrinho}" )
       
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        bairro = request.POST['bairro']
        
        pedido = Pedido.objects.create(nome=nome, telefone=telefone, endereco=endereco, bairro=bairro)
        
        carrinho = request.session.get('carrinho', {})
        for item_id, item in carrinho.items():
            produto_id = int(item_id.split('_')[0])
            produto = get_object_or_404(Produtos, id=produto_id)
            ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=item['quantidade'])
        
        
        # Lógica para enviar os detalhes do pedido para o WhatsApp
        pedido_detalhes = f'Pedido de {nome}:\nTelefone: {telefone}\n'
        for item in pedido.itens.all():
            pedido_detalhes += f'{item.quantidade} x {item.produto.titulo} - R${item.get_total()}\n'
        pedido_detalhes += f'Total do Pedido: R${sum(item.get_total() for item in pedido.itens.all())}'
        
        # Use a API do WhatsApp para enviar os detalhes do pedido
        # Aqui você pode usar uma biblioteca como Twilio para enviar mensagens para o WhatsApp
        # 
        
        # Limpar o carrinho após finalizar o pedido
        request.session['carrinho'] = {}
        print('ok')
        
        return render(request, 'pedido_finalizado.html', {'pedido_detalhes': pedido_detalhes}) 
        
        

    
    return render(request, 'finalizar_pedido.html', context)

def adicionar_ao_carrinho(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        proteinas_ids = request.POST.getlist('proteinas')
        acompanhamentos_ids = request.POST.getlist('acompanhamentos')
        observacao = request.POST.get('observacao', '')
        quantidade = request.POST.get('quantidade', 1)

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
                'id': produto.id,
                'produto': produto.titulo,
                'imagem':produto.capa ,
                'preco': float(produto.valor_promo),  # converter Decimal para float
                'proteinas': [proteina.titulo for proteina in proteinas],
                'acompanhamentos': [acomp.nome for acomp in acompanhamentos],
                'observacao': observacao,
                'quantidade': float(quantidade),
                'total': float(produto.valor_promo) * float(quantidade),
            }
        else:
            # Se já existir, apenas incrementar a quantidade
            carrinho[item_id]['quantidade'] += int(quantidade)

        # Atualizar o carrinho na sessão
        request.session['carrinho'] = carrinho
        for produto, itens in carrinho.items():
            print(f"{produto} \n {itens}")
        # Redirecionar para a página do menu
        return redirect('menu')  # Certifique-se de que a URL 'menu' está configurada corretamente

    return JsonResponse({'error': 'Método não permitido'}, status=405)
    

def cartTeste(request):
    carrinho = request.session.get('carrinho', {})
    total_carrinho = func_total_carrinho(carrinho) # type: ignore

    context = {
        'carrinho': carrinho,
        'total_carrinho': total_carrinho,
    }
    for produto, itens in carrinho.items():
        print(f"{produto} \n {itens}")
        
    return render(request, 'ver_carrinho2.html', context)

