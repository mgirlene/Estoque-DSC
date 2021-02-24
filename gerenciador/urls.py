from django.urls import path
from .views import ProdutoView, EstoqueView

from gerenciador.views import index

urlpatterns = [
    path('index', index, name='index'),
    path('produto/', ProdutoView.as_view(), name="produto"),
    path('estoque/', EstoqueView.as_view(), name="estoque"),

]
