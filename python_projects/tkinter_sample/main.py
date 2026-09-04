from window import App
from db_connection import createTables

if __name__ == "__main__": #comprueba que el archivo ha sido llamado directamente y no importado
    createTables()
    app = App()
    app.mainloop()