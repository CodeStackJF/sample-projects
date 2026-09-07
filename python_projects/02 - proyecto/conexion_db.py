import sqlite3

DB = "usuarios.db"

def conectar():
    return sqlite3.connect(DB)

def crearTablas():
    con = conectar()
    cursor = con.cursor()

    cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    correo TEXT NOT NULL
                )
                """)