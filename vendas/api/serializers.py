from rest_framework import serializers
from ..models import Vendas

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendas
        fields = ['id', 'numero', 'data', 'cliente', 'produto', 'quantidade','usuario']
