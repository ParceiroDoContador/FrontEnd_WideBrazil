const express = require('express');
const cors = require('cors');
const { uploadFile } = require('./bucket');

const app = express();

app.use(cors());
app.use(express.static('public'));


app.get('/s3Url', async (req, res) => {
    const url = await uploadFile();
    res.send({ url });
});



app.listen(8080, () => console.log('Server Up!'));