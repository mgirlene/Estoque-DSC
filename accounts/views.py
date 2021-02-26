from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UsuarioRegisterForm
from .models import CustomUsuario


class LoginView(LoginView):
    template_name = 'login.html'
    success_url = 'index'


class LogoutView(LogoutView):
    template_name = 'index'

def reset(request):
    return render(request, 'reset.html')

class UserCreateView(CreateView):
    model = CustomUsuario
    success_url = 'login'
    template_name = 'cadastroUser.html'
    form_class = UsuarioRegisterForm

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return reverse(self.success_url)


