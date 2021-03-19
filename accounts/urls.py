from django.urls import path, include
from .views import LogoutView, UserCreateView, UserUpdate
from rest_framework import routers
from .api.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'usuario', UserViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('cadastro/', UserCreateView.as_view(), name="cadastrar_usuario"),
    path('editar/<int:pk>/', UserUpdate.as_view(), name="userUpdate"),
]
