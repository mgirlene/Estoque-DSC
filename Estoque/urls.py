from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('gerenciador.urls')),
    path('', include('estoques.urls')),
    path('', include('produtos.urls')),
    path('', include('vendas.urls')),
    path('admin/', admin.site.urls),
]
