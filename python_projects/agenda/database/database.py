import sqlite3


DB = "personas.db"


def conectar():
    return sqlite3.connect(DB)


def crear_tablas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telefonos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona_id INTEGER NOT NULL,
            telefono TEXT NOT NULL,

            FOREIGN KEY (persona_id)
                REFERENCES personas(id)
                ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()