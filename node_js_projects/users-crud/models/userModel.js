const db = require('../config/database');

const UserModel = {
  // Obtener todos los usuarios
  getAll: (callback) => {
    const sql = 'SELECT * FROM users ORDER BY id DESC';
    db.all(sql, [], callback);
  },

  // Obtener un usuario por id
  getById: (id, callback) => {
    const sql = 'SELECT * FROM users WHERE id = ?';
    db.get(sql, [id], callback);
  },

  // Verificar si un email ya existe (opcionalmente excluyendo un id, útil al editar)
  emailExists: (email, excludeId, callback) => {
    let sql = 'SELECT id FROM users WHERE email = ?';
    const params = [email];
    if (excludeId) {
      sql += ' AND id != ?';
      params.push(excludeId);
    }
    db.get(sql, params, callback);
  },

  // Crear un nuevo usuario
  create: (data, callback) => {
    const { first_name, last_name, email, phone_number } = data;
    const sql = `
      INSERT INTO users (first_name, last_name, email, phone_number)
      VALUES (?, ?, ?, ?)
    `;
    db.run(sql, [first_name, last_name, email, phone_number], function (err) {
      callback(err, this ? this.lastID : null);
    });
  },

  // Actualizar un usuario existente
  update: (id, data, callback) => {
    const { first_name, last_name, email, phone_number } = data;
    const sql = `
      UPDATE users
      SET first_name = ?, last_name = ?, email = ?, phone_number = ?
      WHERE id = ?
    `;
    db.run(sql, [first_name, last_name, email, phone_number, id], function (err) {
      callback(err, this ? this.changes : 0);
    });
  },

  // Eliminar un usuario
  delete: (id, callback) => {
    const sql = 'DELETE FROM users WHERE id = ?';
    db.run(sql, [id], function (err) {
      callback(err, this ? this.changes : 0);
    });
  }
};

module.exports = UserModel;
