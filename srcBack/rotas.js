const express = require('express')
const { fazerUpload1, fazerDownload, fazerUploadTexto, fazerUpload4, fazerUpload2, fazerUpload3, login, uploadLog } = require('./controladores/controladores')
const verificaLogin = require('./filtro/validarLogin')

const rotas = express()

rotas.post('/login', login)

rotas.post('/log', uploadLog)

rotas.get('/s3Url1', fazerUpload1)

rotas.get('/s3Url2', fazerUpload2)

rotas.get('/s3Url3', fazerUpload3)

rotas.get('/s3Url4', fazerUpload4)

rotas.get('/s3UrlGet', fazerDownload)

rotas.get('/s3UrlPut', fazerUploadTexto)

module.exports = rotas