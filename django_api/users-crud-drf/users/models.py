from django.db import models


class User(models.Model):
    """Modelo de la tabla users."""

    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Teléfono'
    )
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        db_table = 'users'
        ordering = ['-id']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.first_name} {self.last_name} <{self.email}>'
