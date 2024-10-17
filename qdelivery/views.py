from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import transaction
from django.db.models import Sum
from .models import Dados, Produtos, ItemPedido, Pedido, Acompanhamento, Proteina, Bairro
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import json

#importando funções

from .utils import *

# Create your views here.
def index(request):
    dados = get_object_or_404(Dados, id=1)
    produtos = get_object_or_404(Produtos, id=1)
    quentinhas = Produtos.objects.filter(tipo='Q')
    bebidas = Produtos.objects.filter(tipo='B')
    dados_produto = {
        'dados': dados,
        'produtos': produtos,
        'quentinhas': quentinhas,
        'bebidas': bebidas}
    return render(request, "index.html", dados_produto)
def empresa(request):
    dados = get_object_or_404(Dados, id=1)
    return render(request, "empresa.html", {'dados': dados})
def contatos(request):
    dados = get_object_or_404(Dados, id=1)
    return render(request, "contatos.html", {'dados': dados})
def blog(request):
    dados = get_object_or_404(Dados, id=1)
    return render(request, "blog.html", {'dados': dados})
def cardapio(request):
    identificador = request.session.get('user_id')
    if not identificador:
        criar_identificador(request)
    else:
        ##Pedido.objects.create(identificador_nav=identificador)
        print(f"Identificadortem tem um pedido em aberto no banco: {Pedido.objects.filter(identificador_nav=identificador, status='EM ABERTO').values_list('identificador_nav', flat=True).first()}")
   
    dados = get_object_or_404(Dados, id=1)
    produtos = get_object_or_404(Produtos, id=1)
    quentinhas = Produtos.objects.filter(tipo='Q' ,ativo=True)
    bebidas = Produtos.objects.filter(tipo='B')
    proteinas = Proteina.objects.filter(ativo=True)
    acompanhamento = Acompanhamento.objects.filter(ativo=True)
    cont_cart = ItemPedido.objects.filter(pedido=Pedido.objects.filter(identificador_nav=identificador, status='EM ABERTO').first()).count()
    print("Contagem: ", cont_cart)
    dados_produto = {
        'dados': dados,
        'produtos': produtos,
        'quentinhas': quentinhas,
        'bebidas': bebidas,
        'acompanhamento': acompanhamento,
        'proteinas': proteinas,
        'contagem': cont_cart
        }

    return render(request, "menu.html", dados_produto)

def produto_cardapio(request, id):
    identificador = request.session.get('user_id')
    if not identificador:
        criar_identificador(request)
    else:
        print(f"Identificador já existente: {identificador}")
    

    produto = get_object_or_404(Produtos, id=id)
    dados = get_object_or_404(Dados, id=1)
    dados_produto = {
        'id':produto.id,
        'titulo': produto.titulo,
        'preco': str(produto.valor_promo),
        'tipo': produto.tipo,
        'capa': produto.capa,
        'acompanhamentos': Acompanhamento.objects.filter(ativo=True),
        'proteinas':  Proteina.objects.filter(ativo=True) 
    }
    context = {
        'dados_produto': dados_produto,
        'dados':dados
    }
    return render(request, "produto.html", context)


def produto_detalhes(request, id):
    produto = get_object_or_404(Produtos, id=id)
    
    dados_produto = {
        'titulo': produto.titulo,
        'descricao': produto.descricao,
        'preco': str(produto.valor_promo),
        'tipo': produto.tipo
    }
    return JsonResponse(dados_produto)




def carrinho(request):
    carrinho = request.session.get('carrinho', {})
    total_carrinho = func_total_carrinho(carrinho)


    
    context = {
        'carrinho': carrinho,
        'total_carrinho': total_carrinho,
    }
    return render(request, 'ver_carrinho2.html', context)

""" 
    #Função atualizar antiga

    def atualizar_quantidade(request):
    if request.method == 'POST':
        # Decodifica o corpo da requisição JSON
        data = json.loads(request.body)
        item_id = data.get('item_id')
        quantidade = data.get('quantidade')

        # Obter o carrinho da sessão
        carrinho = request.session.get('carrinho', {})

        # Atualizar a quantidade do item
        if item_id in carrinho:
            carrinho[item_id]['quantidade'] = quantidade
            # Atualizar o total do item
            carrinho[item_id]['total'] = carrinho[item_id]['preco'] * quantidade

        # Atualizar o carrinho na sessão
        request.session['carrinho'] = carrinho
        request.session.modified = True  # Marca a sessão como modificada

        # Calcular o novo total do carrinho
        total_carrinho = sum(item['total'] for item in carrinho.values())

        return JsonResponse({'success': True, 'total_carrinho': total_carrinho})

    return JsonResponse({'error': 'Método não permitido'}, status=405) """



def atualizar_quantidade(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        nova_quantidade = data.get('quantidade')
        pedido_id = data.get('id_pedido')

        try:
            item = ItemPedido.objects.get(id=item_id)
            item.quantidade = nova_quantidade
            item.total = float(item.preco * nova_quantidade)
            item.save()
            total_pedido = ItemPedido.objects.filter(pedido_id=pedido_id).aggregate(Sum('total'))['total__sum'] or 0 # Atualiza o total baseado na nova quantidade
            print("Novo total: ", total_pedido)
            return JsonResponse({'status': 'success', 'nova_quantidade': item.quantidade, 'total': item.total, 'total_pedido': float(total_pedido)})
        except ItemPedido.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item não encontrado'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Método inválido'}, status=400)
    


def remover_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')

        try:
            # Tenta buscar o item a ser removido no banco de dados
            item = get_object_or_404(ItemPedido, id=item_id)
            
            # Remove o item do banco de dados
            item.delete()

            # Opcional: Se quiser, você pode calcular o total do carrinho novamente e retornar
            pedido = item.pedido
            total_carrinho = ItemPedido.objects.filter(pedido=pedido).aggregate(total=Sum('total'))['total']

            return JsonResponse({
                'status': 'success',
                'total_carrinho': float(total_carrinho)
            })

        except ItemPedido.DoesNotExist:
            return JsonResponse({'error': 'Item não encontrado'}, status=404)

    return JsonResponse({'error': 'Método não permitido'}, status=405)



from datetime import datetime
#Views não usadas no ate o momento

def finalizar_pedido(request):
    ##Get banco de dados

    bairro = Bairro.objects.all()

    carrinho = request.session.get('carrinho', {})
    #Valor total do carrinho
    total_carrinho = request.POST.get('total_carrinho')

    context = {
        'bairros': bairro,
        'total_carrinho': total_carrinho
        }
    if request.method == 'POST':
        usuario = request.session.get('usuario', {})
        usuario = {
            'nome': request.POST.get('nome', ''),
            'telefone': request.POST.get('telefone', '')
        }
        #Pedido.objects.create(nome=usuario['nome'], telefone=usuario['telefone'], endereco="Rua Teste")
        context['usuario'] = usuario
        print(f"{datetime.now()}  {usuario} carrinho: {carrinho} \n Total a pagar: {total_carrinho}" )
       
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        bairro = request.POST['bairro']
        
        pedido = Pedido.objects.create(nome=nome, telefone=telefone, endereco=endereco, bairro=bairro)
        
        carrinho = request.session.get('carrinho', {})
        for item_id, item in carrinho.items():
            produto_id = int(item_id.split('_')[0])
            produto = get_object_or_404(Produtos, id=produto_id)
            ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=item['quantidade'])
        
        
        # Lógica para enviar os detalhes do pedido para o WhatsApp
        pedido_detalhes = f'Pedido de {nome}:\nTelefone: {telefone}\n'
        for item in pedido.itens.all():
            pedido_detalhes += f'{item.quantidade} x {item.produto.titulo} - R${item.get_total()}\n'
        pedido_detalhes += f'Total do Pedido: R${sum(item.get_total() for item in pedido.itens.all())}'
        
        # Use a API do WhatsApp para enviar os detalhes do pedido
        # Aqui você pode usar uma biblioteca como Twilio para enviar mensagens para o WhatsApp
        # 
        
        # Limpar o carrinho após finalizar o pedido
        request.session['carrinho'] = {}
        print('ok')
        
        return render(request, 'pedido_finalizado.html', {'pedido_detalhes': pedido_detalhes}) 
        
        

    
    return render(request, 'finalizar_pedido.html', context)

def adicionar_ao_carrinho(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        proteinas_ids = request.POST.getlist('proteinas')
        acompanhamentos_ids = request.POST.getlist('acompanhamentos')
        observacao = request.POST.get('observacoes', '')
        quantidade = int(request.POST.get('quantidade', 1))
        

        try:
            with transaction.atomic():
                # Obter o produto
                produto = get_object_or_404(Produtos, id=produto_id)

                # Obter proteinas e acompanhamentos
                proteinas = Proteina.objects.filter(id__in=proteinas_ids)
                acompanhamentos = Acompanhamento.objects.filter(id__in=acompanhamentos_ids)

                valid_pedido = Pedido.objects.filter(identificador_nav=request.session.get('user_id'), status='EM ABERTO')
                if not valid_pedido.exists():
                    pedido = Pedido.objects.create(identificador_nav=request.session.get('user_id'))
                else:
                    print(f"Pedido já existente para o identificador: {valid_pedido.first().identificador_nav}")
                    pedido = valid_pedido.first()
                ItemPedido.objects.create(
                    pedido=pedido,  # O pedido correspondente
                    produto=produto,
                    imagem=produto.capa,
                    preco=produto.valor_promo,
                    quantidade=quantidade,
                    observacao=observacao,
                    proteinas=[proteina.titulo for proteina in proteinas],  # Lista de proteínas
                    acompanhamentos=[acomp.nome for acomp in acompanhamentos],  # Lista de acompanhamentos
                    total=float(produto.valor_promo) * quantidade
                )
        except Exception as e:
            print(f"Erro ao adicionar item ao carrinho: {e}")
            # Se ocorrer algum erro, a transação será revertida automaticamente
        return redirect('menu')
        """ 
        # Obter ou criar o carrinho na sessão
        carrinho = request.session.get('carrinho', [])

        # Dados do novo item
        novo_item = {
            'id': produto.id,
            'produto': produto.titulo,
            'imagem': produto.capa,
            'preco': float(produto.valor_promo),  # converter Decimal para float
            'proteinas': [proteina.titulo for proteina in proteinas],
            'acompanhamentos': [acomp.nome for acomp in acompanhamentos],
            'observacao': observacao,
            'quantidade': quantidade,
            'total': float(produto.valor_promo) * quantidade,
        }

        # Verificar se o mesmo item (mesmo produto com as mesmas proteínas e acompanhamentos) já está no carrinho
        item_existente = None
        for item in carrinho:
            if (item['id'] == novo_item['id'] and 
                item['proteinas'] == novo_item['proteinas'] and 
                item['acompanhamentos'] == novo_item['acompanhamentos'] 
                ):
                item_existente = item
                break

        if item_existente:
            # Se o item já existir, incrementar a quantidade e atualizar o total
            item_existente['quantidade'] += quantidade
            item_existente['total'] = item_existente['preco'] * item_existente['quantidade']
        else:
            # Se não existir, adicionar o novo item ao carrinho
            carrinho.append(novo_item)

        # Atualizar o carrinho na sessão
        request.session['carrinho'] = carrinho

        for item in carrinho:
            print(item)
              """

        # Redirecionar para a página do menu 
    return JsonResponse({'error': 'Método não permitido'}, status=405)



def cartTeste(request):
    identificador = request.session.get('user_id')
    
    # Buscar o pedido em aberto
    pedido = Pedido.objects.filter(identificador_nav=identificador, status='EM ABERTO').first()
    
    if pedido:
        # Buscar os itens do pedido
        pedido_cart = ItemPedido.objects.filter(pedido=pedido)
        total_carrinho = pedido_cart.aggregate(Sum('total'))['total__sum'] or 0
    else:
        pedido_cart = None

    # Passar os itens do pedido para o contexto
    context = {
        'carrinho': carrinho,
        'total_carrinho': float(total_carrinho),
        'pedido_cart': pedido_cart,
    }

    return render(request, 'ver_carrinho3.html', context)

