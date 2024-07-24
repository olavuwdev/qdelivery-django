from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
def empresa(request):
    return render(request, "empresa.html")
def contatos(request):
    return render(request, "contatos.html")
def blog(request):
    return render(request, "blog.html")
def cardapio(request):
    return render(request, "menu.html")