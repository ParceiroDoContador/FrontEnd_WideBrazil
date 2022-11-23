const express = require('express');
const cors = require('cors');
const fs = require('fs')
const http = require('http')
const path = require('path')
const dotEnv = require('dotenv')
const { secret } = require('../.env')
const session = require('express-session')
const { fazerUpload1, fazerDownload, fazerUploadTexto, fazerUpload4, fazerUpload2, fazerUpload3 } = require('./controladores');

dotEnv.config()

const app = express();
const server = http.createServer(app);

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(session({secret: secret, resave: true, saveUninitialized: true}))





app.use(express.static('public'));

app.use('/srcfront/*', (req, res, next) => {
    if(req.session.email) {
        next()
    } else {
        res.redirect('/page0.html')
    }
})


app.post('/login', (req, res) => {
           const usuarios = fs.readFileSync('./localDB.json')
           const usuariosObj = JSON.parse(usuarios)

           let email = req.body.email
           let senha = req.body.senha

           for(let usuario of usuariosObj) {
                if(email === usuario.email && senha === usuario.senha) {
                     req.session.email = usuario
                     res.send('conectado')
                     return
                }
           }
              res.send('Falhou')
 
});

app.get('/s3Url1', fazerUpload1);

app.get('/s3Url2', fazerUpload2);

app.get('/s3Url3', fazerUpload3);

app.get('/s3Url4', fazerUpload4);

app.get('/s3UrlGet', fazerDownload);

app.get('/s3UrlPut', fazerUploadTexto);


app.listen(8080, () => console.log('Server Up!'));