from window import App
from conexion_db import crearTablas

if __name__ == "__main__":
    crearTablas()
    app = App()
    app.crearVariables()
    app.crearInterfaz()
    app.cargarUsuarios()
    app.mainloop()