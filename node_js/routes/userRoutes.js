const express = require('express');
const router = express.Router();

const UserController = require('../controllers/userController');

router.get('/', UserController.index);
router.get('/new', UserController.newUser);
router.post('/', UserController.create);
router.get('/:id/edit', UserController.editForm);
router.put('/:id', UserController.update);
router.delete('/:id', UserController.delete);

module.exports = router;