# app/management/commands/reset_envios.py
from django.core.management.base import BaseCommand
from ..models import WhatsappContato

class Command(BaseCommand):
    help = 'Reseta os envios para o dia seguinte'

    def handle(self, *args, **kwargs):
        WhatsappContato.objects.update(status='pendente', enviado_em=None, tentativa=0)
        self.stdout.write(self.style.SUCCESS('Envios resetados com sucesso.'))
