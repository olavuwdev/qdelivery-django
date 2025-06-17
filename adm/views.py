from django.shortcuts import render
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WhatsappContato
from django.conf import settings
from django.core.files.storage import default_storage
import tempfile
from decouple import config
import json
import MySQLdb

#VARIAVEIS DO WHATSAPP
evolution_base = config('EVOLUTION_URL_API')
evolution_api_key = config('EVOLUTION_KEY_API')
evolution_api_instance = config('EVOLUTION_INSTANCE_API')
teste_api = config('EVOLUTION_API_TESTE')


def home2(request):
     return render(request, "home/index.html")


def CadastroProduto(request):
    try:
        conn = MySQLdb.connect(
            host="mysql.lunartecnologia.com.br",
            user="lunartecnologi94",
            passwd="Jp5s3KaWvJmsK3HxXgiw",
            db="lunartecnologi94", 
            charset="utf8mb4",
            use_unicode=True,
            # Se estiver usando o MySQL padrão, a porta é 3306
            port=3306
        )
        cursor = conn.cursor()
        
        print("Conexão com o banco de dados estabelecida com sucesso.")
        cursor.close()
        conn.close()

    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return render(request, "home/add-new-food.html")

def WhatsAppAll(request):
     #whatsapps = Whatsapp.objects.all()
      # Busca contatos ativos
     contatos = [{
            'nome': 'João Silva',
            'endereco': 'Rua das Flores, 123',
            'numero': '84988887777',
            'observacao': 'Cliente VIP',
            'status': 'ATIVO'
        },
        {
            'nome': 'Maria Oliveira',
            'endereco': 'Av. Brasil, 456',
            'numero': '84991234567',
            'observacao': '',
            'status': 'ATIVO'
        },
        {
            'nome': 'Carlos Souza',
            'endereco': 'Rua do Comércio, 789',
            'numero': '84999889988',
            'observacao': None,
            'status': 'ATIVO'
        }
        ]
     print(contatos)
     context = {
         'contatos': contatos,
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
        contatos = [{
            'nome': 'João Silva',
            'endereco': 'Rua das Flores, 123',
            'numero': '84988887777',
            'observacao': 'Cliente VIP',
            'status': 'ATIVO'
        },
        {
            'nome': 'Maria Oliveira',
            'endereco': 'Av. Brasil, 456',
            'numero': '84991234567',
            'observacao': '',
            'status': 'ATIVO'
        },
        {
            'nome': 'Carlos Souza',
            'endereco': 'Rua do Comércio, 789',
            'numero': '84999889988',
            'observacao': None,
            'status': 'ATIVO'
        }
        ]
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



@csrf_exempt
def sincronizar_contatos(request):
    if request.method != 'POST':
        return JsonResponse({'mensagem': 'Método não permitido'}, status=405)

    try:
        
        contatos = response.json()
        url = "http://20.206.200.91/chat/findContacts/Qdelivery"

        payload = {"where": {"id": ""}}
        headers = {
            "apikey": "2CAF57B3F559-4FA7-8CB6-C979D0C3EBEC",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        contatos = response.json().get('contacts', [])
        print(f"Contatos: {contatos}")
        criados = 0
        atualizados = 0

        for contato in contatos:
            remote_jid = contato.get('remoteJid', '')
            name = contato.get('name', '')

            if '-' in remote_jid or not remote_jid.endswith('@s.whatsapp.net'):
                continue  # ignora grupos

            numero_completo = remote_jid.replace('@s.whatsapp.net', '')
            ddd = numero_completo[:2]
            numero = numero_completo[2:]

            obj, created = WhatsappContato.objects.update_or_create(
                numero=numero,
                defaults={
                    'nome': name,
                    'ddd': ddd,
                    'status': 'ATIVO'
                }
            )

            if created:
                criados += 1
            else:
                atualizados += 1

        return JsonResponse({
            'mensagem': f'Sincronização concluída. {criados} criados, {atualizados} atualizados.'
        })

    except Exception as e:
        return JsonResponse({'mensagem': 'Erro ao sincronizar contatos', 'erro': str(e)}, status=500)
    
def enviar_cardapio_em_lote(request):
    # Cardápio do dia - pegue a imagem do disco e converta
    caminho_imagem = '/caminho/para/cardapio.jpg'
    with open(caminho_imagem, 'rb') as img:
        imagem_base64 = base64.b64encode(img.read()).decode()

    contatos = WhatsappContato.objects.filter(status='pendente')[:10]
    enviados = []

    for contato in contatos:
        payload = {
            "numero": contato.numero,
            "mensagem": "Olá! Confira o cardápio do dia 📝",
            "tipo": "imagem",
            "imagem": imagem_base64,
            "nome_arquivo": "cardapio.jpg"
        }

        try:
            response = requests.post("https://api.evolution.com.br/enviar", json=payload, timeout=10)
            if response.status_code == 200:
                contato.status = 'enviado'
                contato.enviado_em = timezone.now()
                enviados.append(contato.numero)
            else:
                contato.status = 'erro'
        except Exception as e:
            contato.status = 'erro'

        contato.tentativa += 1
        contato.save()

    return JsonResponse({"enviados": enviados})