from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home2(request):
     return render(request, "home/index.html")
def CadastroProduto(request):
     return render(request, "home/add-new-food.html")