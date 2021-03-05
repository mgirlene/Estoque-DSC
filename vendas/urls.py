from django.urls import path
from .views import VendasView, VendasListView, VendasDeleteView, VendasUpdateView

urlpatterns = [
    path('venda/', VendasView.as_view(), name="venda"),
    path('listarVenda/', VendasListView.as_view(), name='venda_list'),
    path('editarVenda/<int:pk>', VendasUpdateView.as_view(), name='venda_update'),
    path('deletarVenda/<int:pk>/', VendasDeleteView.as_view(), name='venda_delete'),
]