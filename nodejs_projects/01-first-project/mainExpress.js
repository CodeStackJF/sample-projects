const express = require('express')
const app = express();
const square = require('./helpers/square')
app.use(express.json());

app.use((error, req, res, next) => {
    console.error(error.stack);
    res.status(500).send('Something went wrong on our end.');
})

app.get('/tasks', (req, res) => {
    res.json({message: 'list of tasks'})
});

app.post('/tasks', (req, res) => {
    res.send('task created')
});

app.get('/api/tasks/:id', async (req, res, next) => {
    try
    {
        console.log(`Getting task ${id}`)
    }
    catch(error)
    {
        next(error);
    }
});

app.get('/api/square/:width', async (req, res, next) => {
    console.log(req.params.width);
    const width = req.params.width;
    const area = square.area(width)
    res.send(`area es ${area}`);
});

app.listen(3000, function(){
    console.log('Server listening.');
});