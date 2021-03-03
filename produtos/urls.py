from django.urls import path
from .views import ProdutoView,ProdutoDeleteView,ProdutoUpdateView,ProdutoListView

urlpatterns = [
    path('produto/<int:pk>', ProdutoView.as_view(), name="produto"),
    path('listarProdutos/<int:pk>', ProdutoListView.as_view(), name='produto_list'),
    path('editarProduto/<int:pk>', ProdutoUpdateView.as_view(), name='produto_update'),
    path('deletarProduto/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),

]
