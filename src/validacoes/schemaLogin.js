const yup = require('./yupConfig')

const schemaLogin = yup.object().shape({
    email: yup.string().email().required('Obrigatório email e senha'),
    senha: yup.string().required('Obrigatório email e senha')
})

module.exports = schemaLogin