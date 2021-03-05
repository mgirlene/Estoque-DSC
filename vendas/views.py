from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import VendaForm
from .models import Vendas
from produtos.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


class VendasView(LoginRequiredMixin, CreateView):
    model = Vendas
    template_name = 'vendaCreate.html'
    form_class = VendaForm
    success_url = 'venda_list'

    def form_valid(self, form):
        venda = form.save(commit=False)
        venda.cliente = self.request.user
        venda.data = datetime.now()
        id = self.kwargs.get("pk")
        produto_id = Produto.objects.get(id=id)
        venda.produto = produto_id
        venda.save()
        return super(VendasView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Venda cadastrada com sucesso!')
        return reverse(self.success_url)


class VendasListView(LoginRequiredMixin, ListView):
    model = Vendas
    context_object_name = 'vendas_list'
    template_name = 'VendaList.html'



class VendasUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendas
    form_class = VendaForm
    template_name = 'vendaUpdate.html'

    def get_success_url(self):
        for member in Vendas.iterator():
            id = member.id

        return reverse('vendas_list', args=[id])


class VendasDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendas
    template_name = 'vendasDelete.html'

    def get_success_url(self):
        for member in Vendas.iterator():
            id = member.id

        return reverse('vendas_list', args=[id])


