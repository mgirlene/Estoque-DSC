from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import ProdutoForm
from .models import Produto
from gerenciador.models import Categoria
from estoques.models import Estoque

class ProdutoView(CreateView):
    model = Produto
    template_name = 'cadastroProduto.html'
    form_class = ProdutoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TipoCategoria'] = Categoria.objects.all()
        return context

    def form_valid(self, form):
        produto = form.save(commit=False)
        Produto.estoque = Estoque.objects.get(id)
        produto.save()
        return super(ProdutoView, self).form_valid(form)

    def get_success_url(self):
        return reverse('estoqueList')



    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return reverse(self.success_url)
