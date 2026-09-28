const { validationResult } = require('express-validator');
const UserModel = require('../models/userModel');

const UserController = {
  // GET /users -> Listado de usuarios
  index: (req, res) => {
    UserModel.getAll((err, users) => {
      if (err) {
        console.error(err);
        return res.status(500).render('error', { message: 'Error al obtener los usuarios' });
      }
      res.render('users/index', {
        users,
        success: req.query.success || null
      });
    });
  },

  // GET /users/new -> Formulario de creación
  newForm: (req, res) => {
    res.render('users/new', {
      errors: [],
      oldData: {}
    });
  },

  // POST /users -> Guardar nuevo usuario
  create: (req, res) => {
    const errors = validationResult(req);
    const { first_name, last_name, email, phone_number } = req.body;

    if (!errors.isEmpty()) {
      return res.status(400).render('users/new', {
        errors: errors.array(),
        oldData: req.body
      });
    }

    UserModel.emailExists(email, null, (err, row) => {
      if (err) {
        console.error(err);
        return res.status(500).render('error', { message: 'Error al validar el email' });
      }
      if (row) {
        return res.status(400).render('users/new', {
          errors: [{ msg: 'El email ya está registrado por otro usuario' }],
          oldData: req.body
        });
      }

      UserModel.create({ first_name, last_name, email, phone_number }, (err) => {
        if (err) {
          console.error(err);
          return res.status(500).render('users/new', {
            errors: [{ msg: 'Ocurrió un error al crear el usuario' }],
            oldData: req.body
          });
        }
        res.redirect('/users?success=Usuario creado correctamente');
      });
    });
  },

  // GET /users/:id -> Ver detalle de un usuario
  show: (req, res) => {
    const { id } = req.params;
    UserModel.getById(id, (err, user) => {
      if (err) {
        console.error(err);
        return res.status(500).render('error', { message: 'Error al obtener el usuario' });
      }
      if (!user) {
        return res.status(404).render('error', { message: 'Usuario no encontrado' });
      }
      res.render('users/show', { user });
    });
  },

  // GET /users/:id/edit -> Formulario de edición
  editForm: (req, res) => {
    const { id } = req.params;
    UserModel.getById(id, (err, user) => {
      if (err) {
        console.error(err);
        return res.status(500).render('error', { message: 'Error al obtener el usuario' });
      }
      if (!user) {
        return res.status(404).render('error', { message: 'Usuario no encontrado' });
      }
      res.render('users/edit', { user, errors: [], oldData: user });
    });
  },

  // PUT /users/:id -> Actualizar usuario
  update: (req, res) => {
    const { id } = req.params;
    const errors = validationResult(req);
    const { first_name, last_name, email, phone_number } = req.body;

    if (!errors.isEmpty()) {
      return res.status(400).render('users/edit', {
        user: { id, first_name, last_name, email, phone_number },
        errors: errors.array(),
        oldData: req.body
      });
    }

    UserModel.emailExists(email, id, (err, row) => {
      if (err) {
        console.error(err);
        return res.status(500).render('error', { message: 'Error al validar el email' });
      }
      if (row) {
        return res.status(400).render('users/edit', {
          user: { id, first_name, last_name, email, phone_number },
          errors: [{ msg: 'El email ya está registrado por otro usuario' }],
          oldData: req.body
        });
      }

      UserModel.update(id, { first_name, last_name, email, phone_number }, (err, changes) => {
        if (err) {
          console.error(err);
          return res.status(500).render('error', { message: 'Error al actualizar el usuario' });
        }
        if (changes === 0) {
          return res.status(404).render('error', { message: 'Usuario no encontrado' });
        }
        res.redirect('/users?success=Usuario actualizado correctamente');
      });
    });
  },

  // DELETE /users/:id -> Eliminar usuario
  delete: (req, res) => {
    const { id } = req.params;
    UserModel.delete(id, (err, changes) => {
      if (err) {
        console.error(err);
        return res.status(500).render('error', { message: 'Error al eliminar el usuario' });
      }
      if (changes === 0) {
        return res.status(404).render('error', { message: 'Usuario no encontrado' });
      }
      res.redirect('/users?success=Usuario eliminado correctamente');
    });
  }
};

module.exports = UserController;
