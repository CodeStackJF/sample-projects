# Users CRUD — Node.js + Express + SQLite

CRUD sencillo para la tabla `users` con arquitectura MVC y vistas en EJS.

## Estructura del proyecto

```
users-crud/
├── app.js                  # Punto de entrada de la aplicación
├── package.json
├── config/
│   └── database.js         # Conexión a SQLite y creación de la tabla
├── models/
│   └── userModel.js        # Consultas SQL (CRUD) sobre la tabla users
├── controllers/
│   └── userController.js   # Lógica de negocio / manejo de peticiones
├── routes/
│   └── userRoutes.js       # Definición de rutas y validaciones
├── views/                  # Plantillas HTML (EJS)
│   ├── index.ejs
│   ├── error.ejs
│   ├── partials/
│   │   ├── header.ejs
│   │   └── footer.ejs
│   └── users/
│       ├── index.ejs       # Listado
│       ├── new.ejs         # Formulario de creación
│       ├── edit.ejs        # Formulario de edición
│       └── show.ejs        # Detalle
└── public/
    └── css/
        └── style.css        # Estilos
```

## Campos de la tabla `users`

| Campo         | Tipo     | Notas                        |
|---------------|----------|-------------------------------|
| id            | INTEGER  | Autoincremental, primary key |
| first_name    | TEXT     | Obligatorio                  |
| last_name     | TEXT     | Obligatorio                  |
| email         | TEXT     | Obligatorio, **único**       |
| phone_number  | TEXT     | Opcional                     |
| created_on    | DATETIME | Se asigna automáticamente     |

La base de datos SQLite (`database.sqlite`) se crea automáticamente en la raíz del proyecto la primera vez que arrancas la app.

## Instalación

```bash
cd users-crud
npm install
```

## Ejecución

```bash
npm start
```

O en modo desarrollo (con recarga automática, requiere nodemon):

```bash
npm run dev
```

La aplicación quedará disponible en: `http://localhost:3000`

## Rutas disponibles

| Método | Ruta              | Acción                          |
|--------|-------------------|----------------------------------|
| GET    | /users            | Listado de usuarios              |
| GET    | /users/new        | Formulario para crear usuario    |
| POST   | /users            | Crear usuario                    |
| GET    | /users/:id        | Ver detalle de un usuario        |
| GET    | /users/:id/edit   | Formulario para editar usuario   |
| PUT    | /users/:id        | Actualizar usuario (via `_method=PUT`) |
| DELETE | /users/:id        | Eliminar usuario (via `_method=DELETE`) |

Las peticiones PUT/DELETE se envían desde los formularios HTML usando `method-override` con el parámetro `?_method=PUT` / `?_method=DELETE`, ya que los navegadores solo soportan GET y POST en formularios nativos.

## Validaciones

- `first_name`, `last_name`, `email` son obligatorios.
- `email` debe tener formato válido y ser único (se valida tanto a nivel de aplicación con `express-validator` como a nivel de base de datos con la restricción `UNIQUE`).
- Los errores de validación se muestran en el propio formulario.
