from django.contrib import admin

from qdelivery.models import Dados, RedeSocial, Estado, Cidade, Produtos

# Register your models here.
admin.site.register([Dados, RedeSocial, Estado, Cidade, Produtos])