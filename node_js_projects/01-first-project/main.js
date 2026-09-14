const {createServer} = require('node:http');

const hostName = process.env.HOST;
const port = process.env.PORT;

const server = createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'application/json');
    res.end('{"data": "hello world"}')
});

const fs = require('node:fs');
fs.readFile('config.json', 'utf8', (error, data) => {
    if(error)
    {
        console.error('Error reading file:', error);
        return;
    }
    console.log('File content: ', data);
});

console.log('This runs while the file is being read.');

server.listen(port, hostName, () => {
    console.log(`Server running at http://${hostName}:${port}/`);
})