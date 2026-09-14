from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer del modelo User.
    La validación de email único se aplica automáticamente porque el
    campo tiene unique=True en el modelo (DRF genera un UniqueValidator).
    """

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'created_on',
        ]
        read_only_fields = ['id', 'created_on']
