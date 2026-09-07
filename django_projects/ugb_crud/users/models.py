from django.db import models

# Create your models here.

class User(models.Model):

    first_name = models.CharField('First Name', max_length=150)
    last_name = models.CharField('Last Name', max_length=150)
    email = models.CharField('Email', max_length=150)
    phone_number = models.CharField('Phone Number', max_length=150)

    class Meta:
        db_table="users"
        ordering = ["email"]
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'