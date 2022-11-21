const aws = require('aws-sdk');
const dotEnv = require('dotenv');
const { AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY } = require('../.env');

//tentar exportar o fileName do script.js para o bucket.js inves do ao contrario



dotEnv.config();

const region = 'sa-east-1';
const bucketName = 'parceiro-do-contador-bucket'
const accessKeyId = AWS_ACCESS_KEY_ID;
const secretAccessKey = AWS_SECRET_ACCESS_KEY;

const s3 = new aws.S3({
    region,
    accessKeyId,
    secretAccessKey,
    signatureVersion: 'v4',
});

 export const fileName = '';

 async function uploadFile() {
  
    const params = ({
        Bucket: bucketName,
        Key: fileName
    });

    const uploadURL = await s3.getSignedUrlPromise('putObject', params);
    return uploadURL;
}

async function getFile() {

    const params = ({
        Bucket: bucketName,
        Key: fileName,
    });

    const getURL = await s3.getSignedUrlPromise('getObject', params);
    return getURL;
}

async function uploadText() {
    const textName = 'nome_valor.json';

    const params = ({
        Bucket: bucketName,
        Key: textName,
    });

    const uploadURL2 = await s3.getSignedUrlPromise('putObject', params);
    return uploadURL2;
}


module.exports = { uploadFile, getFile, uploadText };