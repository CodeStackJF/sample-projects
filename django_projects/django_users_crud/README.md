# CRUD de Usuarios en Django + SQLite (auth con hash + salt)

Proyecto Django que implementa un CRUD completo sobre una tabla `users`
personalizada, con autenticación propia basada en contraseña **hasheada
(PBKDF2-HMAC-SHA256) + salt** (no usa el modelo `User` de `django.contrib.auth`).

## Modelo `User` (tabla `users`)

| Campo         | Tipo                              | Detalle                                   |
|---------------|-----------------------------------|--------------------------------------------|
| id            | BigAutoField (PK)                 | Autoincremental                            |
| first_name    | CharField(150)                    | Nombres                                    |
| last_name     | CharField(150)                    | Apellidos                                  |
| email         | EmailField(unique)                | Usado para login                           |
| phone_number  | CharField(20)                     | Opcional                                   |
| password      | CharField(256)                    | **Hash** de la contraseña (nunca en claro) |
| salt          | CharField(64)                     | Salt aleatorio único por usuario           |
| status        | CharField choices: active/inactive| Estado de la cuenta                        |
| created_at    | DateTimeField(auto_now_add)       | Fecha de creación                          |

## Cómo funciona la autenticación

- Al crear/editar un usuario con contraseña, `User.set_password()`:
  1. Genera un `salt` aleatorio de 16 bytes (`os.urandom`) en hex.
  2. Calcula `hash = PBKDF2-HMAC-SHA256(password, salt, 260000 iteraciones)`.
  3. Guarda `password = hash` y `salt` en la base de datos. **Nunca se
     guarda la contraseña en texto plano.**
- En el login (`User.check_password()`), se recalcula el hash con el
  salt guardado y la contraseña ingresada, y se compara con
  `hmac.compare_digest` (comparación en tiempo constante, evita timing attacks).
- La sesión de "usuario logueado" se maneja con `request.session`, mediante
  un decorador propio `@login_required_custom` (no se usa
  `django.contrib.auth`, aunque la app sigue instalada para poder usar
  `/admin/`).

## Instalación

```bash
# 1. Crear entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones (crea db.sqlite3 y la tabla `users`)
python manage.py migrate

# 4. (Opcional) Crear un superusuario para /admin/
python manage.py createsuperuser

# 5. Levantar el servidor de desarrollo
python manage.py runserver
```

Abre tu navegador en **http://127.0.0.1:8000/**

## Rutas principales

| Ruta                          | Descripción                                  |
|-------------------------------|-----------------------------------------------|
| `/login/`                     | Inicio de sesión (email + password)           |
| `/register/`                  | Registro público de un nuevo usuario          |
| `/logout/`                    | Cerrar sesión                                 |
| `/users/`                     | Listado de usuarios (requiere sesión)         |
| `/users/nuevo/`                | Crear usuario (requiere sesión)               |
| `/users/<id>/`                | Ver detalle de usuario                        |
| `/users/<id>/editar/`         | Editar usuario (password opcional)            |
| `/users/<id>/eliminar/`       | Eliminar usuario (con confirmación)           |
| `/admin/`                     | Panel de administración de Django             |

## Flujo recomendado para probar

1. Ve a `/register/` y crea tu primer usuario.
2. Inicia sesión en `/login/` con ese email/contraseña.
3. Serás redirigido a `/users/`, donde puedes crear, ver, editar y
   eliminar usuarios (CRUD completo).
4. Verifica en la base de datos (`db.sqlite3`, tabla `users`) que la
   columna `password` contiene un hash largo en hexadecimal y `salt`
   un valor aleatorio distinto por usuario — nunca la contraseña en texto plano.

## Notas de seguridad

- `SECRET_KEY` y `DEBUG=True` están configurados para desarrollo. Cambia
  ambos antes de desplegar a producción.
- Considera usar `argon2` o `bcrypt` (vía `django-passlib` o similar) si
  necesitas cumplir estándares más estrictos; PBKDF2-HMAC-SHA256 con
  260,000 iteraciones ya es una opción robusta y es la que usa Django
  por defecto para su propio sistema de auth.
