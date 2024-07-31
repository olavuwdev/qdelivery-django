from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Dados, Produtos, ItemPedido, Pedido
from django.http import JsonResponse

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
    quentinhas = Produtos.objects.filter(tipo='Q')
    bebidas = Produtos.objects.filter(tipo='B')
    dados_produto = {
        'dados': dados,
        'produtos': produtos,
        'quentinhas': quentinhas,
        'bebidas': bebidas}

    return render(request, "menu.html", dados_produto)

def produto_detalhes(request, id):
    produto = get_object_or_404(Produtos, id=id)
    
    dados_produto = {
        'titulo': produto.titulo,
        'descricao': produto.descricao,
        'preco': str(produto.valor),
        'tipo': produto.tipo,  
    }
    return JsonResponse(dados_produto)




def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produtos, id=produto_id)
    carrinho = request.session.get('carrinho', {})
    
    if produto_id in carrinho:
        carrinho[produto_id]['quantidade'] += 1
    else:
        carrinho[produto_id] = {'titulo': produto.titulo, 'valor': produto.valor, 'quantidade': 1}
    
    request.session['carrinho'] = carrinho
    return redirect('ver_carrinho')

def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    total = sum(item['quantidade'] * item['valor'] for item in carrinho.values())
    return render(request, 'ver_carrinho.html', {'carrinho': carrinho, 'total': total})

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