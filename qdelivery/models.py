from django.db import models

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
    logo = models.CharField(max_length=255)
    icone = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    frete = models.DecimalField(max_digits=10, decimal_places=2)
    cnpj = models.CharField(max_length=100)
    descricao = models.TextField()
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
    usuario = models.IntegerField()
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=70, blank=True, null=True)

    def __str__(self):
        return self.nome

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

