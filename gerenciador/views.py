from django.db.models.sql import query
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from estoques.models import Estoque
from produtos.models import Produto
from vendas.models import Vendas
from django.db.models import Q
from django.db.models import Sum, Count
import json


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

        queryset = Produto.objects.filter(estoque__in=estok)
        names = [obj.nome for obj in queryset]
        context['list_produtos'] = names

        prod_t = Vendas.objects.filter(produto__in=queryset)
        qtd_p = [ob.quantidade for ob in prod_t]
        context['list_qtd'] = qtd_p

        print(queryset)

        chart = [c.nome for c in estok]
        context['list_est'] = chart

        chart2 = [p.quantidade for p in queryset]
        context['list_qtd_prod'] = chart2

        return context
