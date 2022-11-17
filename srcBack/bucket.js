const aws = require('aws-sdk');
const dotEnv = require('dotenv');
const { AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY } = require('../.env');



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

 async function uploadFile() {
   const fileName = 'planilha_wide.pdf';
   

    const params = ({
        Bucket: bucketName,
        Key: fileName,
    });

    const uploadURL = await s3.getSignedUrlPromise('putObject', params);
    return uploadURL;
}

async function getFile() {
    const fileName = 'planilha_wide.pdf';

    const params = ({
        Bucket: bucketName,
        Key: fileName,
    });

    const getURL = await s3.getSignedUrlPromise('getObject', params);
    return getURL;
}



module.exports = { uploadFile, getFile};