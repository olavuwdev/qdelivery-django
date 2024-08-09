

#calcultar total do carrinho

def func_total_carrinho(carrinho):
    total_carrinho = 0
    for item_id, item in carrinho.items():
        item['total'] = item['preco'] * item['quantidade']
        total_carrinho += item['total']
        return total_carrinho