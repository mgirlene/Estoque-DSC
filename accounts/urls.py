from django.urls import path, include

from gerenciador.views import index
from accounts.views import AdminLogin
from accounts.views import CreateUser

urlpatterns = [
    path('login', AdminLogin.as_view(), name='login'),
    path('', CreateUser.as_view(), name= 'cadastrar_usuario'),
]
