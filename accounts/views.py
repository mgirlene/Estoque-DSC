from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse
from django.conf import settings

from django.shortcuts import render
from django.contrib import messages

from Estoque import settings
from accounts.models import CustomUsuario
from accounts.forms import CustomUsuarioForm

class AdminLogin(LoginView):
    template_name = 'login.html'
    success_url = 'gerenciador'


class CreateUser(CreateView):
    model = CustomUsuario
    success_url = 'login'
    template_name = 'cadastroUser.html'
    form_class = CustomUsuarioForm

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return reverse(self.success_url)
