from django.db import models

# Create your models here.
class User(models.Model):

    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.CharField(max_length=255, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Apellido')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        db_table = 'users'
        ordering = ['-id']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email}'

