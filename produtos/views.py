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
    success_url = 'estoqueList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TipoCategoria'] = Categoria.objects.all()
        return context

    def form_valid(self, form):
        produto = form.save(commit=False)
        id = self.kwargs.get("pk")
        estoque_id = Estoque.objects.get(id=id)
        produto.estoque = estoque_id
        produto.save()
        return super(ProdutoView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Produto cadastrado com sucesso!')
        return reverse(self.success_url)


class ProdutoListView(ListView):
    model = Produto
    context_object_name = 'produto_list'
    template_name = 'produtoList.html'


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtoUpdate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TipoCategoria'] = Categoria.objects.all()
        return context

    def get_success_url(self):
        return reverse('produto_list')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtoDelete.html'

    def get_success_url(self):
        return reverse('produto_list')
