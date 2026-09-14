from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    #get /users?search=
    #get/users/{id}
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['id', 'first_name', 'last_name', 'email', 'created_on']