const knex = require('../../BancoDeDados/conexao')
const jwt = require('jsonwebtoken')

const verificaLogin = async (req, res, next) => {
    const { authorization } = req.headers;

    if (!authorization) {
        return res.status(401).json('Você não está logado');
    }

    try {
        const token = authorization.replace('Bearer', '').trim();
        const { id } = jwt.verify(token, process.env.SENHA_JWT);
        const usuario = await knex('usuarios').where({ id }).first();

        if (!usuario) {
            return res.status(404).json('Usuário não encontrado');
        }

        const { senha, ...dadosUsuario } = usuario;

        req.usuario = dadosUsuario;
        next();
    } catch (error) {
        return res.status(400).json(error.message);
    }
}


module.exports = verificaLogin