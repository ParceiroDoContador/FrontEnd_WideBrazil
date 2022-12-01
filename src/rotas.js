const express = require('express')
const { fazerDownload, fazerUploadTexto, login, uploadLog, fazerUpload } = require('./controladores/controladores')
const  verificaLogin  = require('./filtro/verificaLogin.js')

const rotas = express()


rotas.post('/login', login)

rotas.post('/log', uploadLog)

rotas.use(verificaLogin)

rotas.get('/s3UrlGet', fazerDownload)

rotas.get('/s3UrlPut', fazerUploadTexto)

rotas.get('/upload-url', fazerUpload)

module.exports = rotas