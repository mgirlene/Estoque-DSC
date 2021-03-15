from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from .forms import UsuarioRegisterForm
from .models import CustomUsuario

class LogoutView(LogoutView):
    template_name = 'index'


class UserCreateView(CreateView):
    model = CustomUsuario
    success_url = 'login'
    template_name = 'cadastroUser.html'
    form_class = UsuarioRegisterForm

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return reverse(self.success_url)
