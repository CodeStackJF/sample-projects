# Users CRUD — Django REST Framework + SQLite

API REST sencilla para la tabla `users`, con estructura ordenada por responsabilidad.

## Estructura del proyecto

```
users-crud-drf/
├── manage.py
├── requirements.txt
├── config/                     # Configuración del proyecto ("config")
│   ├── settings.py             # Ajustes generales, apps, base de datos
│   ├── urls.py                 # Rutas raíz del proyecto
│   ├── wsgi.py
│   └── asgi.py
└── users/                      # App de usuarios
    ├── models.py                # Modelo User (tabla users)
    ├── serializers.py           # Serializador (validación / transformación JSON)
    ├── views.py                 # "Controladores": UserViewSet (lógica del CRUD)
    ├── urls.py                  # Rutas ("routes") de la app, vía DRF router
    ├── admin.py                 # Registro en el panel de administración
    └── migrations/
        └── 0001_initial.py      # Migración inicial de la tabla
```

## Campos del modelo `User` (tabla `users`)

| Campo         | Tipo           | Notas                          |
|---------------|----------------|----------------------------------|
| id            | BigAutoField   | Autoincremental, primary key    |
| first_name    | CharField(100) | Obligatorio                     |
| last_name     | CharField(100) | Obligatorio                     |
| email         | EmailField     | Obligatorio, **único**          |
| phone_number  | CharField(20)  | Opcional (blank/null permitido) |
| created_on    | DateTimeField  | `auto_now_add=True`             |

## Instalación

```bash
cd users-crud-drf
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Migraciones y arranque

La migración inicial ya viene incluida en `users/migrations/0001_initial.py`, así que solo necesitas aplicarla:

```bash
python manage.py migrate
```

(Opcional) Crear un superusuario para entrar al panel de administración:

```bash
python manage.py createsuperuser
```

Levantar el servidor:

```bash
python manage.py runserver
```

La API quedará disponible en: `http://localhost:8000/api/users/`

Como DRF incluye la "Browsable API", puedes abrir esa misma URL desde el navegador y probar el CRUD con una interfaz HTML automática (formularios incluidos), sin necesidad de Postman.

El panel de administración está en `http://localhost:8000/admin/`.

## Endpoints disponibles

| Método | Ruta                  | Acción                        |
|--------|-----------------------|--------------------------------|
| GET    | /api/users/           | Listar usuarios (paginado)    |
| POST   | /api/users/           | Crear usuario                  |
| GET    | /api/users/{id}/      | Ver detalle de un usuario      |
| PUT    | /api/users/{id}/      | Actualizar usuario (completo)  |
| PATCH  | /api/users/{id}/      | Actualizar usuario (parcial)   |
| DELETE | /api/users/{id}/      | Eliminar usuario                |

Filtros/búsqueda opcionales vía query params:
- `?search=texto` busca en `first_name`, `last_name`, `email`.
- `?ordering=first_name` o `?ordering=-created_on` para ordenar.

## Ejemplo de creación (POST /api/users/)

```json
{
  "first_name": "Juan",
  "last_name": "Pérez",
  "email": "juan.perez@example.com",
  "phone_number": "555-1234"
}
```

Si el email ya existe, DRF responde automáticamente con `400 Bad Request` y un mensaje indicando que el usuario con ese email ya existe (gracias a `unique=True` en el modelo).

## Notas

- Base de datos: SQLite (`db.sqlite3`), se crea al correr `migrate`.
- `DEBUG = True` y `SECRET_KEY` de ejemplo están pensados solo para desarrollo local; cámbialos antes de desplegar a producción.
