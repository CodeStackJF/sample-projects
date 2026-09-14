const express = require('express');
const router = express.Router();
const { body } = require('express-validator');
const UserController = require('../controllers/userController');

// Reglas de validación reutilizables para crear/editar
const userValidationRules = [
  body('first_name')
    .trim()
    .notEmpty().withMessage('El nombre es obligatorio')
    .isLength({ max: 100 }).withMessage('El nombre es demasiado largo'),
  body('last_name')
    .trim()
    .notEmpty().withMessage('El apellido es obligatorio')
    .isLength({ max: 100 }).withMessage('El apellido es demasiado largo'),
  body('email')
    .trim()
    .notEmpty().withMessage('El email es obligatorio')
    .isEmail().withMessage('El email no es válido')
    .normalizeEmail(),
  body('phone_number')
    .optional({ checkFalsy: true })
    .trim()
    .isLength({ max: 20 }).withMessage('El teléfono es demasiado largo')
];

// Listado
router.get('/', UserController.index);

// Formulario de nuevo usuario
router.get('/new', UserController.newForm);

// Crear usuario
router.post('/', userValidationRules, UserController.create);

// Ver detalle
router.get('/:id', UserController.show);

// Formulario de edición
router.get('/:id/edit', UserController.editForm);

// Actualizar usuario (via method-override, se recibe como POST + _method=PUT)
router.put('/:id', userValidationRules, UserController.update);

// Eliminar usuario (via method-override, se recibe como POST + _method=DELETE)
router.delete('/:id', UserController.delete);

module.exports = router;
