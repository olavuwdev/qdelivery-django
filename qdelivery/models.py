from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=75, blank=True, null=True)
    uf = models.CharField(max_length=5, blank=True, null=True)
    regiao = models.CharField(max_length=75, blank=True, null=True)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades', null=True, blank=True)
    nome = models.CharField(max_length=75, blank=True, null=True)
    uf = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.nome


class Dados(models.Model):
    logo = RichTextUploadingField()
    icone = RichTextUploadingField()
    nome = models.CharField(max_length=255)
    subtitulo = RichTextField(blank=True, null=True)
    frete = models.DecimalField(max_digits=10, decimal_places=2)
    cnpj = models.CharField(max_length=100)
    descricao = RichTextField()
    fone = models.CharField(max_length=70, blank=True, null=True)
    whatsapp = models.CharField(max_length=70)
    email = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    cep = models.CharField(max_length=100)
    senha_email = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Dado"
        verbose_name_plural = "Dados"
    #Função para formatar o numero do whatsapp
    def formatar_wtt(self):
        if self.whatsapp:
            numero = self.whatsapp.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
            if len(numero) == 10:  # Ex: 8499666265
                return f"55{numero[:2]}{numero[2:]}"
            elif len(numero) == 11:  # Ex: 84996626265
                return f"55{numero[:2]}{numero[2:]}"
            else:
                return numero
        return ""

class RedeSocial(models.Model):
    icone = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    tipo = models.CharField(max_length=70)
    tipo_cadastro = models.CharField(max_length=50, blank=True, null=True)
    data = models.DateTimeField()
    dia = models.CharField(max_length=2, blank=True, null=True)
    mes = models.CharField(max_length=2, blank=True, null=True)
    ano = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    TIPO_CHOICES = [
    ('Q', 'Quentinha'),
    ('B', 'Bebidas'),
    ]
    titulo = models.CharField(max_length=255)
    capa = models.ImageField(upload_to='uploads/')
    valor = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    valor_promo = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    descricao = RichTextField(blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class Acompanhamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    imagem = RichTextUploadingField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
class Proteina(models.Model):
    titulo = models.CharField(max_length=200,unique=True)
    imagem = RichTextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Bairro(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    identificador = models.CharField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome  # Retorna o nome do cliente ao representar o objeto como string


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relação de chave estrangeira com o Cliente
    status = models.CharField(max_length=50, blank=False, default='EM ABERTO')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido de {self.cliente.nome}'  # Mostra o nome do cliente no pedido

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.titulo}'

    def get_total(self):
        return self.quantidade * self.produto.valor

class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)  # Relação de chave estrangeira com o Cliente
    status = models.CharField(max_length=10, default='aberto')
    identificador = models.CharField(max_length=255, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Carrinho N° {self.id}'  # Mostra o nome do cliente associado ao carrinho







    
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, null=True, blank=True,)  # Alterado para relacionar ao produto
    quantidade = models.IntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True)
    proteinas = models.ManyToManyField(Proteina)  # ManyToManyField para armazenar várias proteínas
    acompanhamentos = models.ManyToManyField(Acompanhamento)  # ManyToManyField para vários acompanhamentos

    # Novos campos para armazenar proteínas, acompanhamentos e imagem
    

    def save(self, *args, **kwargs):
        self.preco_total = self.quantidade * self.preco_unitario
        super(ItemCarrinho, self).save(*args, **kwargs)