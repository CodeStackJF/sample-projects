"""
Configuración de Django para el proyecto config (CRUD de Users con auth por hash+salt).
"""

from pathlib import Path

# Construye rutas dentro del proyecto así: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# SEGURIDAD
# --------------------------------------------------------------------------
# ¡ADVERTENCIA! No usar esta clave en producción, generar una nueva.
SECRET_KEY = 'django-insecure-CAMBIA-ESTA-CLAVE-EN-PRODUCCION-1234567890'

# ¡ADVERTENCIA! No dejar DEBUG activado en producción.
DEBUG = True

ALLOWED_HOSTS = ['*']

# --------------------------------------------------------------------------
# APLICACIONES
# --------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # App propia con el CRUD de usuarios y autenticación custom
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Context processor propio: inyecta el usuario logueado (custom auth)
                'users.context_processors.current_user',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# --------------------------------------------------------------------------
# BASE DE DATOS (SQLite)
# --------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------------------------------
# VALIDACIÓN DE CONTRASEÑAS (para el auth interno de Django /admin)
# --------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------------------------------
# INTERNACIONALIZACIÓN
# --------------------------------------------------------------------------
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/El_Salvador'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------
# ARCHIVOS ESTÁTICOS
# --------------------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Mapea los tags de django.contrib.messages a clases de alertas de Bootstrap
from django.contrib.messages import constants as messages_constants  # noqa: E402

MESSAGE_TAGS = {
    messages_constants.DEBUG: 'secondary',
    messages_constants.INFO: 'info',
    messages_constants.SUCCESS: 'success',
    messages_constants.WARNING: 'warning',
    messages_constants.ERROR: 'danger',
}

# --------------------------------------------------------------------------
# CONFIGURACIÓN DE AUTENTICACIÓN CUSTOM (tabla users, sesión propia)
# --------------------------------------------------------------------------
# URL a la que se redirige cuando una vista protegida por @login_required_custom
# detecta que no hay sesión activa.
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'user_list'
LOGOUT_REDIRECT_URL = 'login'

# Parámetros del algoritmo de hash de contraseñas (PBKDF2-HMAC-SHA256)
PASSWORD_HASH_ALGORITHM = 'sha256'
PASSWORD_HASH_ITERATIONS = 260000
