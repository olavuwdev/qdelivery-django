from django.db import models

# Create your models here.
class Whatsapp(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome or 'Sem nome'} - {self.numero}"