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
        'titulo': produto.titulo,
        'preco': str(produto.valor),
        'tipo': produto.tipo,
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
        'preco': str(produto.valor),
        'tipo': produto.tipo
    }
    return JsonResponse(dados_produto)



def adicionar_ao_carrinho(request, produto_id):
    if request.method == "POST":
        dados = json.loads(request.body)
        proteinas_ids = dados.get('proteinas', [])
        acompanhamentos_ids = dados.get('acompanhamentos', [])
        observacoes = dados.get('observacoes', '')

        produto = get_object_or_404(Produtos, id=produto_id)
        
        # Recuperar o carrinho do cookie, ou criar um novo se não existir
        carrinho = json.loads(request.COOKIES.get('carrinho', '{}'))

        # Gerar uma chave única para o item com base no produto e suas seleções
        item_key = f"{produto_id}-{','.join(proteinas_ids)}-{','.join(acompanhamentos_ids)}"

        if item_key in carrinho:
            carrinho[item_key]['quantidade'] += 1
        else:
            carrinho[item_key] = {
                'titulo': produto.titulo,
                'valor': str(produto.valor),
                'quantidade': 1,
                'proteinas': proteinas_ids,
                'acompanhamentos': acompanhamentos_ids,
                'observacoes': observacoes
            }

        response = JsonResponse({'status': 'success'})

        # Armazenar o carrinho atualizado no cookie
        response.set_cookie('carrinho', json.dumps(carrinho), max_age=604800)  # 1 semana de duração

        return response
    

def ver_carrinho(request):
    carrinho = json.loads(request.COOKIES.get('carrinho', '{}'))
    
    # Carregar informações detalhadas sobre proteínas e acompanhamentos
    for item_key, item in carrinho.items():
        item['proteinas'] = Proteina.objects.filter(id__in=item['proteinas'])
        item['acompanhamentos'] = Acompanhamento.objects.filter(id__in=item['acompanhamentos'])
    
    return render(request, 'ver_carrinho.html', {'carrinho': carrinho})



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