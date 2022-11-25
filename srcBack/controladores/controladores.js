const {uploadFile, getFile, uploadText} = require('../bucket')
const knex = require('../../BancoDeDados/conexao')
const bcrypt = require('bcrypt')
const jwt = require('jsonwebtoken')
const schemaLogin = require('../validacoes/schemaLogin')


const uploadLog = async (req, res) => {
    const { nome } = req.body
    const dataDoUpload = new date()
    try {
        const log = await knex('log').insert({nome, dataDoUpload})
        res.status(200).send({ log });
    } catch (error) {
        return res.status(400).json(error.message)
    }
}

const fazerUpload1 = async (req, res) => {
    try {
        const url = await uploadFile('import1/','planilha_teste.pdf');
    res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }
}

const fazerUpload2 = async (req, res) => {
    try {
        const url = await uploadFile('Import2/','nome_valor.json');
    res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }
}

const fazerUpload3 = async (req, res) => {
    try {
        const url = await uploadFile('Import3/','nome_valor.json');
    res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }
}

const fazerUpload4 = async (req, res) => {
    try {
        const url = await uploadFile('Import4/','nome_valor.json');
    res.status(200).send({ url });
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
    console.log(usuario);
    

    if (!usuario) {
      return res.status(404).json({ mensagem: 'Usuário não encontrado' })
    }
    const senhaCorreta = await bcrypt.compare(senha, usuario.senha)

    if (!senhaCorreta) {
      return res.status(400).json({ mensagem: 'Email ou senha não conferem' })
    }
    const token = jwt.sign({ id: usuario.id },SENHA_JWT, { expiresIn: '8h' })
    console.log(token);

    const { senha: _, ...dadosUsuario } = usuario

    return res.status(200).json({
         usuario: dadosUsuario, 
         token 
        })

    } catch (error) {
        return res.status(400).json(error.message)
    }
}


module.exports = { fazerUpload1,fazerUpload2,fazerUpload3,fazerUpload4,fazerDownload, fazerUploadTexto, login, uploadLog}