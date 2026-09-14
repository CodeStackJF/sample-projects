from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'created_on'
        ]
        read_only_field = ['id', 'created_on']