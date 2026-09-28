# Users CRUD — Android (Java) + SQLite

App Android nativa (Java, sin Room) que implementa el mismo CRUD de `users`
que las versiones Node.js/Express y Django REST Framework: `id`, `first_name`,
`last_name`, `email` (único), `phone_number`, `created_on`.

## Estructura del proyecto

```
UsersCRUD/
├── build.gradle                     # Config raíz de Gradle
├── settings.gradle
├── gradle.properties
├── gradle/wrapper/gradle-wrapper.properties
└── app/
    ├── build.gradle                 # Dependencias del módulo app
    ├── proguard-rules.pro
    └── src/main/
        ├── AndroidManifest.xml      # Declaración de Activities (≈ "routes")
        ├── java/com/example/userscrud/
        │   ├── config/
        │   │   └── DatabaseHelper.java     # Conexión SQLite + creación de tabla
        │   ├── models/
        │   │   ├── User.java                # Entidad (POJO)
        │   │   └── UserDao.java             # CRUD sobre SQLite
        │   ├── controllers/
        │   │   ├── MainActivity.java        # Listado (index)
        │   │   ├── UserFormActivity.java     # Crear / Editar (new+create / edit+update)
        │   │   └── UserDetailActivity.java   # Detalle (show)
        │   └── adapters/
        │       └── UserAdapter.java          # Adaptador del RecyclerView
        └── res/
            ├── layout/                        # "Vistas" (equivalente a las .ejs)
            │   ├── activity_main.xml
            │   ├── item_user.xml
            │   ├── activity_user_form.xml
            │   └── activity_user_detail.xml
            └── values/
                ├── strings.xml
                ├── colors.xml
                └── themes.xml
```

## Equivalencia con el proyecto Node.js

| Node.js / Express              | Android (Java)                          |
|---------------------------------|------------------------------------------|
| `config/database.js`            | `config/DatabaseHelper.java`             |
| `models/userModel.js`           | `models/User.java` + `models/UserDao.java` |
| `controllers/userController.js` | `controllers/*Activity.java`             |
| `routes/userRoutes.js`          | `AndroidManifest.xml` (Activities) + `Intent` para navegar entre pantallas |
| `views/*.ejs`                   | `res/layout/*.xml`                        |
| SQLite (archivo `.sqlite`)      | SQLite (archivo `users.db` en el dispositivo, vía `SQLiteOpenHelper`) |

La diferencia clave es que Android no tiene "rutas HTTP": la navegación entre
pantallas se hace con `Intent` (ej. `startActivity(new Intent(this, UserFormActivity.class))`),
y cada `Activity` cumple el rol de un "controlador" que reacciona a una acción del usuario
en vez de a una petición HTTP.

## Cómo abrirlo en Android Studio

1. Descomprime el zip.
2. Abre Android Studio → **File > Open** → selecciona la carpeta `UsersCRUD`.
3. Android Studio detectará que falta el archivo binario `gradle-wrapper.jar`
   (no se puede generar sin conexión a internet desde este entorno) y te
   ofrecerá **regenerarlo automáticamente** al sincronizar. Acepta el prompt,
   o bien corre manualmente, si tienes Gradle instalado:
   ```bash
   gradle wrapper --gradle-version 8.4
   ```
4. Deja que Gradle sincronice (descargará las dependencias de `app/build.gradle`).
5. Ejecuta la app (▶) en un emulador o dispositivo físico (Android 7.0 / API 24 en adelante).

## Funcionalidad implementada

- **Listado** (`MainActivity`): muestra todos los usuarios en un `RecyclerView`,
  con botón flotante (+) para crear uno nuevo, y botones "Editar"/"Eliminar" por fila.
- **Crear / Editar** (`UserFormActivity`): un mismo formulario sirve para ambos casos,
  según si llega o no un `id` en el `Intent`. Valida campos obligatorios, formato de
  email, y captura el error de email duplicado (restricción `UNIQUE` de SQLite).
- **Detalle** (`UserDetailActivity`): muestra los datos completos de un usuario,
  incluyendo `created_on`.
- **Eliminar**: se confirma con un `AlertDialog` antes de borrar.

## Base de datos

Se crea automáticamente la primera vez que se abre la app, en el almacenamiento
privado de la app dentro del dispositivo/emulador (no es un archivo que tú manipules
directamente, a diferencia del `database.sqlite` de la versión Node). Puedes inspeccionarla
con **Android Studio > View > Tool Windows > App Inspection > Database Inspector**
mientras la app está corriendo.
