from django.urls import path, include
from .views import LoginView, LogoutView, UserCreateView, PasswordResetView

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('cadastro/', UserCreateView.as_view(), name="cadastrar_usuario"),
    path('reset/', PasswordResetView.as_view, name="reset"),
]
