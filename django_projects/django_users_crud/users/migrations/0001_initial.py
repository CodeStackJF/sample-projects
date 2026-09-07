from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name='Teléfono')),
                ('password', models.CharField(max_length=256, verbose_name='Password (hash)')),
                ('salt', models.CharField(max_length=64, verbose_name='Salt')),
                (
                    'status',
                    models.CharField(
                        choices=[('active', 'Activo'), ('inactive', 'Inactivo')],
                        default='active',
                        max_length=10,
                        verbose_name='Estado',
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'users',
                'ordering': ['-created_at'],
            },
        ),
    ]
