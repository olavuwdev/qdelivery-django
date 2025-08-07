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
from adm import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new


urlpatterns = [
    path('', views.home2),
    path('addProduto', views.CadastroProduto, name="add-produto"),
    path('fazer-pedido', views.criar_pedido, name="fazer-pedido"),
    path('api/produtos/', views.api_produtos, name='api_produtos'),
    path('api/clientes/', views.api_clientes, name='api_clientes'),
    path('whastapp/allClient', views.WhatsAppAll, name="whatsapp-all"),
    path('whastapp/sendAll', views.send_for_all, name="send-all"),
    path('whastappSend/', views.enviar_mensagens, name="whatsapp-send"),
    path('sincronizar-contatos/', views.sincronizar_contatos, name='sincronizar_contatos'),
    path('conta/receber', views.conta_receber, name='conta_receber'),
    path('conta/receber/form', views.conta_receber_form, name='conta_receber_form'),
]
urlpatterns +=  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
urlpatterns +=  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    