const express = require('express');
const userRoutes = require('./routes/userRoutes');
const methodOverride = require('method-override');
const path = require('path');
require('./config/database');

const app = express();
const PORT = process.env.PORT || 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.urlencoded({extended: true}));
app.use(express.json());
app.use(methodOverride('_method'));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => res.render('index'));
app.use('/users', userRoutes)


app.listen(PORT, () => {
    console.log('Servidor corriendo')
});