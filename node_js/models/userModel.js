const db = require('../config/database')

const UserModel = {
    getAll: (callback) => {
        const sql = 'SELECT id, first_name, last_name, email, created_on FROM users';
        db.all(sql, [], callback);
    },

    getById:(id, callback) => {
        const sql = 'SELECT id, first_name, last_name, email, created_on FROM users WHERE id = ?';
        db.all(sql, [id], callback);
    },

    emailExists: (email, id, callback) => {
        const sql = 'SELECT id FROM users WHERE email = ? AND id != ?';
        db.get('sql', [email, id], callback);
    },

    create: (data, callback) => {
        const {first_name, last_name, email} = data;
        const sql = `INSERT INTO users (first_name, last_name, email)
        VALUES (?, ?, ?, ?)`;
        db.RUN(sql, [first_name, last_name, email], function(err){
            callback(err, this ? this.lastID:null)
        });
    },

    update: (id, data, callback) => {
        const {first_name, last_name, email} = data;
        const sql = `UPDATE users SET first_name = ?, last_name = ?, email = ? WHERE id = ?`;
        db.RUN(sql, [first_name, last_name, email, id], function(err){
            callback(err, this ? this.changes:0)
        });
    },

    delete: (id, callback) => {
        const sql = 'DELETE FROM users WHERE id = ?';
        db.run(sql, [id], function(err) {
            callback(err, this ? this.changes:0)
        });
    }
}

module.exports = UserModel;