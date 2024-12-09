"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from qdelivery import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new


urlpatterns = [
    path('admin/', admin.site.urls),

    path('adm/', include("adm.urls")),
    path('', views.index),
    path('empresa/', views.empresa),
    path('contatos/', views.contatos),
    path('blog/', views.blog, name='blog'),
    path('cardapio/', views.cardapio, name='menu'),
    #path('prod/<int:id>', views.produto_cardapio, name="pro_cardapio"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('ver_carrinho/', views.cartTeste, name='ver_carrinho'),
    #path('ver_carrinho/', views.carrinho, name='ver_carrinho'),


    path('ver_carTeste/', views.carrinho, name='cartTeste'),


    path('adicionar_ao_carrinho/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('produto/<int:id>/', views.produto_detalhes, name='produto_detalhes'), #não usado


    path('atualizar_quantidade/', views.atualizar_quantidade, name='atualizar_quantidade'),
    path('remover_item/', views.remover_item, name='remover_item'),
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
    path('send_email/', views.sendmail_contact, name='send_email'),


    #Rotas para o novo template
    path('new/', views.indexNew , name='new'),
    path('newEmpresa/', views.empresaNew , name='newEmpresa'),
    path('newCardapio/', views.cardapioNew , name='newCardapio'),
    path('newContato/', views.contatosNew , name='newContato'),
    path('prod2/<int:id>', views.produto_cardapio2, name="pro_cardapio"),
    path('newCart/', views.newCart, name="newCart"),
    path('tamanho/', views.tamanho, name="tamanho"),

]
urlpatterns +=  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
urlpatterns +=  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    

admin.site.site_header = 'ADM Quentinha Delivery'
admin.site.index_title = 'Quentinha Delivery'
admin.site.site_title = 'ADM'
