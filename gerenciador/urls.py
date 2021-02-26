from django.urls import path
from .views import ProdutoView, EstoqueView,EstoqueDeleteView,EstoqueListView,EstoqueUpdateView

from gerenciador.views import index

urlpatterns = [
    path('index', index, name='index'),
    path('produto/', ProdutoView.as_view(), name="produto"),
    path('estoque/', EstoqueView.as_view(), name="estoque"),
    path('listar/', EstoqueListView.as_view(), name='estoqueList'),
    path('editar/<int:pk>', EstoqueUpdateView.as_view(), name='estoque_update'),
    path('deletar/<int:pk>/', EstoqueDeleteView.as_view(), name='estoque_delete'),

]
