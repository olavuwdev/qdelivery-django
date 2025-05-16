from django.db import models

# Create your models here.
class Whatsapp(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')], default='ATIVO')

    def __str__(self):
        return f"{self.nome or 'Sem nome'} - {self.numero}"
class WhatsappContato(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=20, unique=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    status = models.CharField(max_length=10, default='ATIVO')

    class Meta:
        db_table = 'qd_ctt_wts'
