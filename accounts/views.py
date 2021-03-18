from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LogoutView
from .forms import UsuarioRegisterForm
from .models import CustomUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

class LogoutView(LogoutView):
    template_name = 'index'


class UserCreateView(CreateView):
    model = CustomUsuario
    success_url = 'login'
    template_name = 'cadastroUser.html'
    form_class = UsuarioRegisterForm

    def form_valid(self, form):
        self.usuario = form.save()

        send_mail(
            'Cadastro Em Stock Control',
            '%s, Você foi cadastrado com sucesso!' % self.usuario.first_name,
            'estoquedsc@gmail.com',
            [self.usuario.email],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return reverse(self.success_url)

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = CustomUsuario
    fields = ('first_name', 'last_name')
    template_name = 'update_user.html'
    success_url = reverse_lazy('index')