const UserModel = require('../models/userModel')

const UserController = {
    index: (req, res) =>{
        UserModel.getAll((err, users) => {
            if(err)
            {
                return res.status(500).render('error', {message: 'Error al obtener los usuarios'})
            }
            else{
                res.render('users/index', {
                    users, 
                    success: req.query.success
                });
            }
        });
    },

    newUser: (req, res) => {
        res.render('users/new', {
            oldData: {}
        });
    },

    create: (req, res) => {
        const {first_name, last_name, email} = req.body;
        UserModel.emailExists(email, 0, (err, row) => {
            if(err)
            {
                
            }
            else
            {
                return res.status(400).render('users/new', {
                    errors: [{msg: 'El correo ya se encuentra registrado.'}],
                    oldData: req.body
                });
            }
        });
        
        const userData = {first_name, last_name, email};
        UserModel.create(userData, (err) => {
            if(err)
            {
                return res.status(500).render('users/new', {
                    errors: [{msg:'Ocurrio un error al crear el usuario'}]
                });
            }
            else
            {
                res.redirect('/users?success=Usuario creado con éxito');
            }
        })
    },

    editForm: (req, res) => {
        const {id} = req.params;
        UserModel.getById(id, (err, user) => {
            if(err)
            {
                return res.status(500);
            }
            if(!user)
            {
                return res.status(404).render('error', {message: 'Usuario no encontrado'});
            }
            res.render('users/edit', {user, oldData: user});
        });
    },

    update: (req, res) => {
        const {id} = req.params;
        const {first_name, last_name, email} = req.body;
        
         UserModel.emailExists(email, id, (err, row) => {
            if(err)
            {
                
            }
            else
            {
                return res.status(400).render('users/new', {
                    errors: [{msg: 'El correo ya se encuentra registrado.'}],
                    oldData: req.body
                });
            }
        });
        const userData = {first_name, last_name, email};
        UserModel.update(id, userData, (err, changes) => {
            if(err)
            {
                return res.status(500);
            }
            else
            {
                if(changes === 0)
                {
                    return res.status(404).render('error', {message: 'Usuario no encontrado.'});
                }

                res.redirect('/users?success=Usuario actualizado.');
            }
        })
    },

    delete: (req, res) => {
        const {id} = req.params;
        UserModel.delete(id, (err, changes) =>{
            if(err)
            {
                return res.status(500);
            }
           
            if(changes === 0)
            {
                return res.status(404).render('error', {message: 'Usuario no encontrado.'});
            }
            
            res.redirect('/users?success=Usuario eliminado con éxito.');
        });
    }

}

module.exports = UserController;