from rest_framework import viewsets, filters

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet que expone el CRUD completo de User:

    GET    /api/users/          -> listar
    POST   /api/users/          -> crear
    GET    /api/users/{id}/     -> detalle
    PUT    /api/users/{id}/     -> actualizar completo
    PATCH  /api/users/{id}/     -> actualizar parcial
    DELETE /api/users/{id}/     -> eliminar
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['id', 'first_name', 'last_name', 'created_on']
