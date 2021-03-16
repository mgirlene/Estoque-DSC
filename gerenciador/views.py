from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from estoques.models import Estoque
from produtos.models import Produto
from vendas.models import Vendas
from django.db.models import Q
from django.db.models import Sum

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        estoque = Estoque.objects.get(usuario=self.request.user.id)
        return estoque

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        est = Estoque.objects.filter(Q(usuario=self.request.user.id)).count()
        context['list_estoque'] = est
        estok = Estoque.objects.filter(Q(usuario=self.request.user.id))
        prod = Produto.objects.filter(estoque__in=estok).aggregate(qtd=Sum('quantidade'))['qtd']
        context['list_produto'] = prod
        venda = Vendas.objects.filter(Q(usuario=self.request.user.id)).count()
        context['list_venda'] = venda
        return context

