const sqlite3 = require('sqlite3');
const path = require('path');

const DB_PATH = path.join(__dirname, '..', 'database.sqlite');

const db = new sqlite3.Database(DB_PATH, (err) => {
    if(err)
    {
        console.log('Error al conectar a la base de datos', err.message);
    }
    else{
        console.log('Conectado a la base de datos en: ', DB_PATH);
    }
});

const createTable = `
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        created_on DATETIME DEFAULT CURRENT_TIMESTAMP
    )
`;

db.serialize(()=>{
    db.run(createTable, (err) => {
        if(err)
        {
            console.log('Error al crear tabla users');
        }
        else
        {
            console.log('Tabla users creada');
        }
    })
});

module.exports = db;