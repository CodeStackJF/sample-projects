from functools import wraps

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

SESSION_USER_ID_KEY = 'auth_user_id'


def login_required_custom(view_func):
    """
    Decorador propio (no usa django.contrib.auth) que exige que exista un
    usuario autenticado en la sesión, validado contra la tabla `users`
    mediante password hash + salt en la vista de login.
    """

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get(SESSION_USER_ID_KEY):
            messages.warning(request, 'Debes iniciar sesión para continuar.')
            login_url = getattr(settings, 'LOGIN_URL', 'login')
            return redirect(f'{login_url}?next={request.path}')
        return view_func(request, *args, **kwargs)

    return _wrapped_view
