from django.contrib import admin
from qdelivery.models import Dados, RedeSocial, Estado, Cidade, Produtos, Acompanhamento, Proteina, Bairro, Pedido

# Registro de modelos sem configurações especiais
admin.site.register([Dados, RedeSocial, Estado, Cidade, Bairro, Pedido])

# Classe de administração para o modelo Acompanhamento
@admin.register(Acompanhamento)
class AcompanhamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    actions = ['marcar_ativos', 'desmarcar_ativos']

    def marcar_ativos(self, request, queryset):
        queryset.update(ativo=True)
        self.message_user(request, "Acompanhamentos marcados como ativos.")

    def desmarcar_ativos(self, request, queryset):
        queryset.update(ativo=False)
        self.message_user(request, "Acompanhamentos desmarcados como inativos.")

    marcar_ativos.short_description = "Marcar acompanhamentos selecionados como ativos"
    desmarcar_ativos.short_description = "Desmarcar acompanhamentos selecionados como inativos"

# Classe de administração para o modelo Produtos
@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'descricao')

@admin.register(Proteina)
class ProteinasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo')
    actions = ['marcar_ativos', 'desmarcar_ativos']

    def marcar_ativos(self, request, queryset):
        queryset.update(ativo=True)
        self.message_user(request, "Acompanhamentos marcados como ativos.")

    def desmarcar_ativos(self, request, queryset):
        queryset.update(ativo=False)
        self.message_user(request, "Acompanhamentos desmarcados como inativos.")

    marcar_ativos.short_description = "Marcar proteinas selecionados como ativos"
    desmarcar_ativos.short_description = "Desmarcar proteinas selecionados como inativos"
