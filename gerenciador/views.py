from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProdutoForm, EstoqueForm
from .models import estoque,produto, categoria

def index(request):
    return render(request, 'index.html')

class ProdutoView(CreateView):
    model = produto
    success_url = 'login'
    template_name = 'cadastroProduto.html'
    form_class = ProdutoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TipoCategoria'] = categoria.objects.all()
        return context

    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return reverse(self.success_url)

class EstoqueView(CreateView):
    model = estoque
    success_url = 'login'
    template_name = 'cadastroEstoque.html'
    form_class = EstoqueForm

    def get_success_url(self):
        messages.success(self.request, 'estoque cadastrado com sucesso!')
        return reverse(self.success_url)


