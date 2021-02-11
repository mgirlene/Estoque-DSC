from django.urls import path, include
from .views import LoginView, LogoutView, UserCreateView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', UserCreateView.as_view(), name="cadastrar_usuario"),
]
