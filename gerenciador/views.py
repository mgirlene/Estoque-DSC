from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import ProdutoForm, EstoqueForm
from .models import estoque, produto, categoria


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
    success_url = 'index'
    template_name = 'cadastroEstoque.html'
    form_class = EstoqueForm

    def form_valid(self, form):
        estoque = form.save(commit=False)
        estoque.usuario = self.request.user

        estoque.save()
        return super(EstoqueView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Estoque cadastrado com sucesso!')
        return reverse(self.success_url)


class EstoqueListView(ListView):
    model = estoque
    context_object_name = 'estoque_list'
    template_name = 'estoqueList.html'


class EstoqueUpdateView(UpdateView):
    model = estoque
    form_class = EstoqueForm
    template_name = 'estoqueUpdate.html'

    def get_success_url(self):
        return reverse('estoqueList')


class EstoqueDeleteView(DeleteView):
    model = estoque
    template_name = 'estoqueDelete.html'

    def get_success_url(self):
        return reverse('estoqueList')
