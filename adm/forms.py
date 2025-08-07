from django import forms


class PedidoForm(forms.Form):
    PRODUTO_CHOICES = [
        ('quentinha_carne', 'Quentinha de Carne - R$ 15,00'),
        ('quentinha_frango', 'Quentinha de Frango - R$ 12,00'),
    ]
    COMPLEMENTO_CHOICES = [
        ('arroz', 'Arroz'),
        ('feijao', 'Feijão'),
        ('macarrao', 'Macarrão'),
        ('batata_frita', 'Batata Frita'),
        ('carne_moida', 'Carne Moída'),
        ('frango_grelhado', 'Frango Grelhado'),
    ]
    
    produto = forms.ChoiceField(choices=PRODUTO_CHOICES, widget=forms.Select)
    complementos = forms.MultipleChoiceField(
        choices=COMPLEMENTO_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
