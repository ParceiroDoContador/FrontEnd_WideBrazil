const knex = require('knex')({        
    client: 'pg',
    connection: {
        host: 'localhost',
        user: 'postgres',
        password: 'parceiroroot',
        database: 'wide_db'
    }
})

module.exports = knex