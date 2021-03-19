from rest_framework import viewsets
from ..models import CustomUsuario
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUsuario.objects.all()
    serializer_class = UserSerializer