const express = require('express');
const cors = require('cors');
const { uploadFile, getFile, uploadText} = require('./bucket');

const app = express();

app.use(cors());
app.use(express.static('public'));

app.get('/s3Url', async (req, res) => {
    const url = await uploadFile();
    res.send({ url });
});

app.get('/s3UrlGet', async (req, res) => {
    const url2 = await getFile();
    res.send({ url2 });
});

app.get('/s3UrlPut', async (req, res) => {
    const url3 = await uploadText();
    res.send({ url3 });
});


app.listen(8080, () => console.log('Server Up!'));