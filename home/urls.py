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
from django.urls import include, path
from qdelivery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('empresa/', views.empresa),
    path('contatos/', views.contatos),
    path('blog/', views.blog, name='blog'),
    path('cardapio/', views.cardapio),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('produto/<int:id>/', views.produto_detalhes, name='produto_detalhes'),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('ver_carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ADM Quentinha Delivery'
admin.site.index_title = 'Quentinha Delivery'
admin.site.site_title = 'ADM'
