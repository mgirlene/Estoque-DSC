from django.urls import path, include
from .views import EstoqueView, EstoqueDeleteView, EstoqueListView, EstoqueUpdateView
from rest_framework import routers
from .api.viewsets import EstoqueViewSet

router = routers.DefaultRouter()
router.register(r'estoque', EstoqueViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('estoque/', EstoqueView.as_view(), name='estoque'),
    path('listar/', EstoqueListView.as_view(), name='estoqueList'),
    path('editar/<int:pk>', EstoqueUpdateView.as_view(), name='estoque_update'),
    path('deletar/<int:pk>/', EstoqueDeleteView.as_view(), name='estoque_delete'),
]
