require('dotenv').config()
const express = require('express')
const cors = require('cors')
const rotas = require('./rotas')

const app = express();

app.use(cors());
app.use(express.json());
app.use("/static", express.static(__dirname + '/static'));
app.use(rotas);


app.listen(process.env.PORT, () => {
  console.log(`Server running`)
});