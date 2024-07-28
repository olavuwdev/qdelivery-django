from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Dados, Produtos
from django.http import JsonResponse

# Create your views here.
def index(request):
    dados = get_object_or_404(Dados, id=1)
    produtos = Produtos.objects.all()
    return render(request, "index.html", {'dados': dados, 'produtos':produtos})
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
        
    }
    return render(request, "menu.html",{'dados': dados,
        'produtos': produtos,
        'quentinhas': quentinhas,
        'bebidas': bebidas})

