from django.urls import path
from .views import ProdutoView

urlpatterns = [
    path('produto/', ProdutoView.as_view(), name="produto"),

]
