from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from estoques.models import Estoque
from produtos.models import Produto
from django.db.models import Q


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        estoque = Estoque.objects.get(usuario=self.request.user.id)
        return estoque

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        est = Estoque.objects.filter(Q(usuario=self.request.user.id)).count()
        context['list_estoque'] = est
        p = Produto.objects.filter(Q(estoque = est)).count()
        context['list_produto'] = p
        return context
