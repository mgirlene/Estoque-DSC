from django.urls import path, include
from .views import VendasView, VendasListView, VendasDeleteView, VendasUpdateView

from rest_framework import routers
from .api.viewsets import VendaViewSet

router = routers.DefaultRouter()
router.register(r'venda', VendaViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('venda/<int:pk>', VendasView.as_view(), name="venda"),
    path('listarVenda/', VendasListView.as_view(), name='venda_list'),
    path('editarVenda/<int:pk>', VendasUpdateView.as_view(), name='venda_update'),
    path('deletarVenda/<int:pk>/', VendasDeleteView.as_view(), name='venda_delete'),
]
