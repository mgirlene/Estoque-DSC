from rest_framework import viewsets
from ..models import Vendas
from .serializers import VendaSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Vendas.objects.all()
    serializer_class = VendaSerializer