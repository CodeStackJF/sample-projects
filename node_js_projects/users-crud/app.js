const express = require('express');
const path = require('path');
const methodOverride = require('method-override');

const userRoutes = require('./routes/userRoutes');
require('./config/database'); // Inicializa la conexión y crea la tabla

const app = express();
const PORT = process.env.PORT || 3000;

// Motor de plantillas
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middlewares
app.use(express.urlencoded({ extended: true })); // Parsear formularios HTML
app.use(express.json());
app.use(methodOverride('_method')); // Soporte para PUT/DELETE desde formularios HTML
app.use(express.static(path.join(__dirname, 'public'))); // Archivos estáticos (CSS)

// Rutas
app.get('/', (req, res) => res.render('index'));
app.use('/users', userRoutes);

// 404
app.use((req, res) => {
  res.status(404).render('error', { message: 'Página no encontrada' });
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
