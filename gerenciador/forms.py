from django.forms import ModelForm
from .models import produto, estoque


class ProdutoForm(ModelForm):
    class Meta:
        model = produto
        fields = ('nome', 'data_validade', 'preco', 'quantidade', 'categoria', 'estoque')

    def save(self, commit=True):
        p = super(ProdutoForm, self).save()
        p.estoque= self.cleaned_data['estoque']
        p.categoria = self.cleaned_data['categoria']

        if commit:
            p.save()
        return p


class EstoqueForm(ModelForm):
    class Meta:
        model = estoque
        fields = ['nome']
