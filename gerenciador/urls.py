from django.urls import path

from gerenciador.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
