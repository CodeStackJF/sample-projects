import sqlite3

DB =  "users.db"

def connect():
    return sqlite3.connect(DB)

def createTables():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       first_name TEXT NOT NULL,
                       last_name TEXT NOT NULL,
                       email TEXT NOT NULL UNIQUE
                   )
                   """)