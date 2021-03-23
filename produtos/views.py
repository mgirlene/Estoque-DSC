from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import ProdutoForm
from .models import Produto
from gerenciador.models import Categoria
from estoques.models import Estoque
from django.contrib.auth.mixins import LoginRequiredMixin


class ProdutoView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'cadastroProduto.html'
    form_class = ProdutoForm

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
        id_p = self.kwargs.get("pk")
        estoque_id = list(produto.estoque.id for produto in Produto.objects.filter(id=id_p))
        produto = Produto.objects.filter(id__in=estoque_id)

        for member in produto.iterator():
            id = member.id
        return reverse('produto_list', args=[id_p])



class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = 'produto_list'
    template_name = 'produtoList.html'

    def get_queryset(self):
        id = self.kwargs.get("pk")
        estoque_id = list(estoque.id for estoque in Estoque.objects.filter(id=id))
        produto = Produto.objects.filter(estoque__in=estoque_id)
        return produto


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtoUpdate.html'

    def get_success_url(self):
        id_p = self.kwargs.get("pk")
        estoque_id = list(produto.estoque.id for produto in Produto.objects.filter(id=id_p))
        produto = Produto.objects.filter(id__in=estoque_id)

        for member in produto.iterator():
            id = member.id
        return reverse('produto_list', args=[id])


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produtoDelete.html'

    def get_success_url(self):
        id_p = self.kwargs.get("pk")
        estoque_id = list(produto.estoque.id for produto in Produto.objects.filter(id=id_p))
        produto = Produto.objects.filter(id__in=estoque_id)

        for member in produto.iterator():
            id = member.id
        return reverse('produto_list', args=[id])
