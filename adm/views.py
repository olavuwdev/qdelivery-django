from django.shortcuts import render
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Whatsapp
from django.conf import settings
from django.core.files.storage import default_storage
import tempfile
from decouple import config
import json

# Create your views here.
def home2(request):
     return render(request, "home/index.html")
def CadastroProduto(request):
     return render(request, "home/add-new-food.html")

def WhatsAppAll(request):
     whatsapps = Whatsapp.objects.all()
     print(whatsapps)
     context = {
         'contatos': whatsapps,
     }
     return render(request, "whatsapp/allClients.html" , context)

evolution_base = config('evolution_base', default='http://olavodev.zapto.org')
evolution_api_key = config('evolution_api_key')
def enviar_mensagens(request):
    if request.method == 'POST':
        ids = json.loads(request.POST.get('ids', '[]'))
        texto = request.POST.get('mensagem', '').strip()
        imagem = request.FILES.get('imagem', None)

        contatos = Whatsapp.objects.filter(id__in=ids)
        resultados = []

        headers = {
            'apikey': evolution_api_key,
            'Content-Type': 'application/json'
        }

        # Se houver imagem, salva temporariamente e gera URL
        imagem_url = ''
        if imagem:
            temp_path = default_storage.save(imagem.name, imagem)
            imagem_url = request.build_absolute_uri(default_storage.url(temp_path))

        for contato in contatos:
            try:
                if imagem_url:
                    # Envia imagem com legenda
                    media_payload = {
                        "number": contato.numero,
                        "mediatype": "image",
                        "mimetype": imagem.content_type,
                        "caption": texto or '',
                        "media": imagem_url,
                        "fileName": imagem.name
                    }
                    url = f"{evolution_base}/message/sendMedia/Qdelivery"
                    r = requests.post(url, json=media_payload, headers=headers, timeout=10)
                else:
                    # Apenas texto
                    text_payload = {
                        "number": contato.numero,
                        "text": texto
                    }
                    r = requests.post(f"{evolution_base}/message/sendText/Qdelivery", json=text_payload, headers=headers, timeout=10)

                r.raise_for_status()
                status = "✅ Enviado"
            except Exception as e:
                status = f"❌ Erro: {str(e)[:80]}"

            resultados.append({
                "numero": contato.numero,
                "nome": contato.nome,
                "status": status
            })

        return JsonResponse({ "resultados": resultados })

    return JsonResponse({ "error": "Método não permitido" }, status=405)