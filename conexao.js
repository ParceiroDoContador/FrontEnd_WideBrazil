const knex = require('knex')({
    client: 'pg',
    connection: {
      host:"localhost",
      user: "postgres",
      password: "240608041009Asa!",
      database: "wide_brazil_db"
      // ssl: { rejectUnauthorized: false }
    }
  })
  
  module.exports = knex