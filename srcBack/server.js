const express = require('express');
const cors = require('cors');
const { knex } = require('knex')
const { fazerUpload1, fazerDownload, fazerUploadTexto, fazerUpload4, fazerUpload2, fazerUpload3, verificarLogin } = require('./controladores/controladores');


const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static('public'));


app.post('/login', verificarLogin); 
    
app.get('/s3Url1', fazerUpload1);

app.get('/s3Url2', fazerUpload2);

app.get('/s3Url3', fazerUpload3);

app.get('/s3Url4', fazerUpload4);

app.get('/s3UrlGet', fazerDownload);

app.get('/s3UrlPut', fazerUploadTexto);


app.listen(8080, () => console.log('Server Up!'));