from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'users',
                'ordering': ['-id'],
            },
        ),
    ]
