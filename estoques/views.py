from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import EstoqueForm
from .models import Estoque
from django.contrib.auth.mixins import LoginRequiredMixin

class EstoqueView(LoginRequiredMixin,CreateView):
    model = Estoque
    success_url = 'estoqueList'
    template_name = 'cadastroEstoque.html'
    form_class = EstoqueForm

    def form_valid(self, form):
        Estoque = form.save(commit=False)
        Estoque.usuario = self.request.user

        Estoque.save()
        return super(EstoqueView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Estoque cadastrado com sucesso!')
        return reverse(self.success_url)


class EstoqueListView(LoginRequiredMixin,ListView):
    model = Estoque
    context_object_name = 'estoque_list'
    template_name = 'estoqueList.html'

    def get_queryset(self):
        estoques = Estoque.objects.order_by('nome').filter(usuario=self.request.user)
        return estoques


class EstoqueUpdateView(LoginRequiredMixin,UpdateView):
    model = Estoque
    form_class = EstoqueForm
    template_name = 'estoqueUpdate.html'

    def get_success_url(self):
        return reverse('estoqueList')


class EstoqueDeleteView(LoginRequiredMixin,DeleteView):
    model = Estoque
    template_name = 'estoqueDelete.html'

    def get_success_url(self):
        return reverse('estoqueList')
