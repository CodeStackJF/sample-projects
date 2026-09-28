const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// Ruta del archivo de la base de datos (se crea automáticamente si no existe)
const DB_PATH = path.join(__dirname, '..', 'database.sqlite');

const db = new sqlite3.Database(DB_PATH, (err) => {
  if (err) {
    console.error('Error al conectar con SQLite:', err.message);
  } else {
    console.log('Conectado a la base de datos SQLite en:', DB_PATH);
  }
});

// Habilitar llaves foráneas (buena práctica, aunque aquí no se usen)
db.run('PRAGMA foreign_keys = ON');

// Creación de la tabla users si no existe
const createTableSQL = `
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT,
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP
  )
`;

db.serialize(() => {
  db.run(createTableSQL, (err) => {
    if (err) {
      console.error('Error al crear la tabla users:', err.message);
    } else {
      console.log('Tabla "users" lista.');
    }
  });
});

module.exports = db;
