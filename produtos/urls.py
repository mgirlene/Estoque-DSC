from django.urls import path, include
from .views import ProdutoView,ProdutoDeleteView,ProdutoUpdateView,ProdutoListView

from rest_framework import routers
from .api.viewsets import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produto', ProdutoViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('produto/<int:pk>', ProdutoView.as_view(), name="produto"),
    path('listarProdutos/<int:pk>', ProdutoListView.as_view(), name='produto_list'),
    path('editarProduto/<int:pk>', ProdutoUpdateView.as_view(), name='produto_update'),
    path('deletarProduto/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),

]
