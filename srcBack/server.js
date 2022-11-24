require('dotenv').config()
const express = require('express')
const cors = require('cors')
const rotas = require('./rotas')

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static('public'));
app.use(rotas);


app.listen(process.env.PORT);