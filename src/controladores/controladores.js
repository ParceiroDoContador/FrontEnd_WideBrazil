const {uploadFile, getFile, uploadText} = require('../bucket')
const knex = require('../../BancoDeDados/conexao')
const jwt = require('jsonwebtoken')
const schemaLogin = require('../validacoes/schemaLogin')
const { pythonRunDecimo, pythonRunFerias, pythonRunFlash, pythonRunInvoice, pythonRunSeguro } = require('./child')


const uploadLog = async (req, res) => {
    const { nome } = req.body
    const data = new Date()
    
    try {
        const log = await knex('logarquivos').insert({nome, data})
        res.status(200).send({ log });
    } catch (error) {
        return res.status(400).json(error.message)
    }
}

 function getFileName(folderNumber) {
    let fileName = "";
    let pythonScript = "";

    switch(folderNumber) {
        case '1' : {
            fileName = "férias.pdf";
            pythonScript = pythonRunFerias()
            break
            
        }

        case '2' : {
            fileName = "décimo.pdf";
            pythonScript = pythonRunDecimo()
            break
            
        }

        case '3' : {
            fileName = "flash.pdf";
            pythonScript = pythonRunFlash()
            break
            
    }
        case '4' :{
            fileName = "seguro.pdf";
            pythonScript = pythonRunSeguro()
            break
    }
   
}
    return fileName, pythonScript;
}

const fazerUpload = async (req, res) => {
    const { folderNumber } = req.query;

    try {
        if (!folderNumber) {
            return res.status(400).json({ error: "Informe o numero da pasta" })
        }

        let fileName = getFileName(folderNumber);
        let pythonScript = getFileName(folderNumber);

        if (!fileName) {
            return res.status(400).json({ error: "Número de pasta inválido" })
        }

        const url = await uploadFile(`import${folderNumber}/`, fileName);
        pythonScript
        return res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }
}

const fazerDownload = async (req, res) => {
        try {
            const url2 = await getFile();
        res.status(200).send({ url2 });
        } catch (error) {
            console.log(error);
            return res.status(400).send({ error: 'Erro ao fazer download do arquivo' });
        }
    }

const fazerUploadTexto = async (req, res) => {
        try {
            const url3 = await uploadText();
            res.status(200).send({ url3 });
            } catch (error) {
                console.log(error);
                return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
            }
}

const login = async (req, res) => {
  const { email, senha } = req.body

  if (!email || !senha) {
    return res.status(400).json('Email e senha são obrigatórios')
  }
  
  try {
    await schemaLogin.validate(req.body)
    const usuario = await knex('usuarios').where({ email }).first()

    if (!usuario) {
      return res.status(404).json({ mensagem: 'Usuário não encontrado' })
    }

    const senhaCorreta = senha === usuario.senha

    if (!senhaCorreta) {
      return res.status(400).json({ mensagem: 'Email ou senha não conferem' })
    }

    const token = jwt.sign({ id: usuario.id },process.env.SENHA_JWT, { expiresIn: '7d' })
    
    const { senha: _, ...dadosUsuario } = usuario
    
    return res.status(200).json({
         usuario: dadosUsuario, 
         token 
        })
    } catch (error) {
        console.log(error)
        return res.status(400).json(error.message)
    }
}

module.exports = { fazerDownload, fazerUploadTexto, login, uploadLog, fazerUpload}