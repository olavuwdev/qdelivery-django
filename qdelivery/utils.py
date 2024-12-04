from bs4 import BeautifulSoup
import uuid

from django.http import HttpResponse

#calcular total do carrinho

def func_total_carrinho(carrinho):
    total_carrinho = 0
    for item in carrinho:
        item['total'] = item['preco'] * item['quantidade']
        total_carrinho += item['total']
        return total_carrinho
    

#Gerar um codigo identificado aleatorio    
def gerar_identificador_unico():
    return str(uuid.uuid4())
def criar_identificador(request):
        identificador = gerar_identificador_unico()
        request.session['user_id'] = identificador  # Armazena o identificador na sessão
        response = HttpResponse("Cookie definido com sucesso!")
        response.set_cookie('user_id', identificador, max_age=60*60*24*365)  # Cookie válido por 1 ano
        print(f"Identificador criado: {identificador}")


def extrair_src(html):
    """
    Extrai o valor do atributo 'src' de uma tag <img> em um string HTML.
    """
    soup = BeautifulSoup(html, 'html.parser')
    img_tag = soup.find('img')  # Encontra a tag <img>
    if img_tag and 'src' in img_tag.attrs:
        return img_tag['src']  # Retorna o valor do atributo 'src'
    return None  # Retorna None se não encontrar
