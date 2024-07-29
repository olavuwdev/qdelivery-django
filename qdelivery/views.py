from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Dados, Produtos
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


