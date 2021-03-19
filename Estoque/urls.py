from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title=' API`s Estoque DSC ')

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('gerenciador.urls')),
    path('', include('estoques.urls')),
    path('', include('produtos.urls')),
    path('', include('vendas.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view),

]
