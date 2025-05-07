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

#VARIAVEIS DO WHATSAPP
evolution_base = config('EVOLUTION_URL_API')
evolution_api_key = config('EVOLUTION_KEY_API')
evolution_api_instance = config('EVOLUTION_INSTANCE_API')
teste_api = config('EVOLUTION_API_TESTE')


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



#Enviar mensagens para todos os contatos ativos
@csrf_exempt
def send_for_all(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        texto = request.POST.get('mensagem', '').strip()
        imagens = request.FILES.get('imagens', None)

        # Busca contatos ativos
        contatos = Whatsapp.objects.filter(status='ATIVO')

        resultados = []

        headers = {
            'apikey': evolution_api_key,
            'Content-Type': 'application/json'
        }

        imagem_url = ''
        if imagens:
            temp_path = default_storage.save(imagens.name, imagens)
            imagem_url = request.build_absolute_uri(default_storage.url(temp_path))

        for contato in contatos:
            try:
                if imagem_url:
                    # Envio de imagem
                    media_payload = {
                        "number": contato.numero,
                        "mediatype": "image",
                        "mimetype": imagens.content_type,
                        "caption": texto or '',
                        "media": 'http://lunartecnologia.com.br/hoje_tem_feijoada.png',
                        "fileName": imagens.name
                    }
                    url = f"{evolution_base}/message/sendMedia/{evolution_api_instance}"
                    print(f"URL: {url}")
                    print(f"Payload: {media_payload}")
                    r = requests.post(url, json=media_payload, headers=headers, timeout=10)
                else:
                    # Envio de texto
                    text_payload = {
                        "number": contato.numero,
                        "text": texto
                    }
                    url = f"{evolution_base}/message/sendText/{evolution_api_instance}"
                    r = requests.post(url, json=text_payload, headers=headers, timeout=10)

                r.raise_for_status()
                status = "✅ Enviado"
            except Exception as e:
                status = f"❌ Erro: {str(e)[:80]}"

            resultados.append({
                "numero": contato.numero,
                "nome": contato.nome,
                "status": status
            })

        return JsonResponse({"resultados": resultados})

    return JsonResponse({"error": "Método não permitido"}, status=405)


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
                    url = f"{EVOLUTION_BASE_URL}/message/sendMedia/Qdelivery"
                    r = requests.post(url, json=media_payload, headers=headers, timeout=10)
                else:
                    # Apenas texto
                    text_payload = {
                        "number": contato.numero,
                        "text": texto
                    }
                    r = requests.post(f"{EVOLUTION_BASE_URL}/message/sendText/Qdelivery", json=text_payload, headers=headers, timeout=10)

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

