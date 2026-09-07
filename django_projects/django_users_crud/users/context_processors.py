from .decorators import SESSION_USER_ID_KEY
from .models import User


def current_user(request):
    """
    Expone `auth_user` en todos los templates: el usuario autenticado según
    nuestra sesión propia (independiente de django.contrib.auth).
    """
    user_id = request.session.get(SESSION_USER_ID_KEY)
    if not user_id:
        return {'auth_user': None}
    try:
        return {'auth_user': User.objects.get(pk=user_id)}
    except User.DoesNotExist:
        return {'auth_user': None}
