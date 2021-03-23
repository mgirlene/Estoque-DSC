from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import VendaForm
from .models import Vendas
from produtos.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.db.models import Sum

class VendasView(LoginRequiredMixin, CreateView):
    model = Vendas
    template_name = 'vendaCreate.html'
    form_class = VendaForm
    success_url = 'venda_list'

    def form_valid(self, form):
        venda = form.save(commit=False)
        venda.data = datetime.now()
        id = self.kwargs.get("pk")
        produto_id = Produto.objects.get(id=id)
        venda.produto = produto_id
        ano_corrente = datetime.now()
        venda.numero = f"{ano_corrente.year}00{id}"
        venda.usuario = self.request.user
        qtd_produto = form.cleaned_data["quantidade"]
        sub_qtd = Produto.objects.filter(id=id).aggregate(qtd=Sum('quantidade'))['qtd']
        total = sub_qtd - qtd_produto
        Produto.objects.filter(id=id).update(quantidade=total)
        venda.save()
        return super(VendasView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com sucesso!')
        return reverse(self.success_url)


class VendasListView(LoginRequiredMixin, ListView):
    model = Vendas
    context_object_name = 'venda_list'
    template_name = 'VendaList.html'

    def get_queryset(self):
        vendas = Vendas.objects.order_by('data').filter(usuario=self.request.user)
        return vendas


class VendasUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendas
    form_class = VendaForm
    template_name = 'vendaUpdate.html'

    def get_success_url(self):
        return reverse('vendas_list')


class VendasDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendas
    template_name = 'vendaDelete.html'

    def get_success_url(self):
        return reverse('venda_list')
