from rest_framework import serializers
from ..models import CustomUsuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsuario
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
