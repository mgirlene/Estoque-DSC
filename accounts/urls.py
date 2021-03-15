from django.urls import path, include
from .views import LogoutView, UserCreateView

urlpatterns = [
    path('logout/', LogoutView.as_view(), name="logout"),
    path('cadastro/', UserCreateView.as_view(), name="cadastrar_usuario"),
]
