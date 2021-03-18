from django.urls import path

from gerenciador.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('vendas-chart/', IndexView.vendas_chart, name='vendas-chart'),
    path('estoques-chart/', IndexView.estoques_chart, name='estoques-chart'),
]
