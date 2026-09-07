import binascii
import hashlib
import hmac
import os

from django.conf import settings
from django.db import models


# ---------------------------------------------------------------------------
# Utilidades de hashing de contraseñas (PBKDF2-HMAC-SHA256 + salt aleatorio)
# ---------------------------------------------------------------------------
def generate_salt(length: int = 16) -> str:
    """Genera un salt aleatorio criptográficamente seguro, en hexadecimal."""
    return binascii.hexlify(os.urandom(length)).decode('utf-8')


def hash_password(raw_password: str, salt: str) -> str:
    """
    Deriva un hash de la contraseña en texto plano usando el salt dado,
    mediante PBKDF2-HMAC-SHA256 (recomendado por OWASP para almacenamiento
    de contraseñas cuando no se usa bcrypt/argon2).
    """
    algorithm = getattr(settings, 'PASSWORD_HASH_ALGORITHM', 'sha256')
    iterations = getattr(settings, 'PASSWORD_HASH_ITERATIONS', 260000)
    derived_key = hashlib.pbkdf2_hmac(
        algorithm,
        raw_password.encode('utf-8'),
        salt.encode('utf-8'),
        iterations,
    )
    return binascii.hexlify(derived_key).decode('utf-8')


class User(models.Model):
    """
    Tabla `users` personalizada (no es el modelo de auth de Django).
    Guarda el password ya hasheado junto a su salt individual; nunca se
    almacena ni se compara la contraseña en texto plano.
    """

    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo'),
    ]

    first_name = models.CharField('Nombres', max_length=150)
    last_name = models.CharField('Apellidos', max_length=150)
    email = models.EmailField('Correo electrónico', unique=True)
    phone_number = models.CharField('Teléfono', max_length=20, blank=True)
    password = models.CharField('Password (hash)', max_length=256)
    salt = models.CharField('Salt', max_length=64)
    status = models.CharField(
        'Estado', max_length=10, choices=STATUS_CHOICES, default=STATUS_ACTIVE
    )
    created_at = models.DateTimeField('Creado el', auto_now_add=True)

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.first_name} {self.last_name} <{self.email}>'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def is_active(self):
        return self.status == self.STATUS_ACTIVE

    # ------------------------------------------------------------------
    # Manejo de contraseña: nunca se guarda en texto plano.
    # ------------------------------------------------------------------
    def set_password(self, raw_password: str) -> None:
        """Genera un nuevo salt y guarda el hash de la contraseña dada."""
        self.salt = generate_salt()
        self.password = hash_password(raw_password, self.salt)

    def check_password(self, raw_password: str) -> bool:
        """Valida una contraseña en texto plano contra el hash almacenado."""
        if not self.password or not self.salt:
            return False
        candidate_hash = hash_password(raw_password, self.salt)
        # Comparación en tiempo constante para evitar timing attacks.
        return hmac.compare_digest(candidate_hash, self.password)
