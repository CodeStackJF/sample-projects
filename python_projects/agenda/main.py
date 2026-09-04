from database.database import crear_tablas
from views.ventana import Aplicacion


if __name__ == "__main__":
    crear_tablas()

    app = Aplicacion()
    app.mainloop()