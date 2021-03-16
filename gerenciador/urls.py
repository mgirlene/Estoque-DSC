from django.urls import path

from gerenciador.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
]
