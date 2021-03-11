from django.forms import ModelForm
from .models import Vendas


class VendaForm(ModelForm):
    class Meta:
        model = Vendas
        fields = ['quantidade', 'cliente']