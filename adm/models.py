from django.db import models

# Create your models here.


class WhatsappContato(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=20, unique=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    status = models.CharField(max_length=10, default='ATIVO')

    class Meta:
        db_table = 'qd_ctt_wts'
