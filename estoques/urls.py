from django.urls import path
from .views import EstoqueView, EstoqueDeleteView, EstoqueListView, EstoqueUpdateView

urlpatterns = [
    path('estoque/', EstoqueView.as_view(), name='estoque'),
    path('listar/', EstoqueListView.as_view(), name='estoqueList'),
    path('editar/<int:pk>', EstoqueUpdateView.as_view(), name='estoque_update'),
    path('deletar/<int:pk>/', EstoqueDeleteView.as_view(), name='estoque_delete'),
]
