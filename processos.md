* ACOMPANHAMENTO DE PROCESSOS DO SISTEMA *


1- CRIAR UM IDENTIFICADOR UNICO

2 - ARMAZENAR O ESSE IDENTIFICADOR EM UM COOKIE

3 - SALVAR ESSA INFORMAÇÃO NO BANCO DE DADOS 

4 - VERIFICAR SE JÁ EXISTE UM CARRINHO ABERTO PARA ESSE USUARIO

    class Carrinho(models.MOdel):
        usuario_id
        nome_usuario = models.CharField(max_length=150, default='')
        status = models.CharField(max_length=10, default='aberto')
        data_criacao = models.DateTimeField(auto_now_add=True)
        data_modificacao = models.DateTimeField(auto_now=True)


    class ItemCarrinho(models.Model):
        carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
        produto_id = models.IntegerField()
        quantidade = models.IntegerField(default=1)
        preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
        preco_total = models.DecimalField(max_digits=10, decimal_places=2)

5 - SE NÃO EXISTER CRIAR UM CARRINHO PARA O USUARIO 

6 - SE EXISTIR ACRESCENTAR O ITEM NO carrinho