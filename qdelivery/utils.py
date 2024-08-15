import uuid

from django.http import HttpResponse

#calcular total do carrinho

def func_total_carrinho(carrinho):
    total_carrinho = 0
    for item_id, item in carrinho.items():
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