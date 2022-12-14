const aws = require('aws-sdk');
const dotEnv = require('dotenv');

dotEnv.config();

const region = 'sa-east-1';
const bucketName = 'parceiro-do-contador-bucket'
const accessKeyId = process.env.AWS_ACCESS_KEY_ID;
const secretAccessKey = process.env.AWS_SECRET_ACCESS_KEY;

const s3 = new aws.S3({
    region,
    accessKeyId,
    secretAccessKey,
    signatureVersion: 'v4',
});

 async function uploadFile(folderName,fileName) {
  
    let params = ({
        Bucket: bucketName,
        Key: `${folderName}${fileName}`,
    });

    const uploadURL = await s3.getSignedUrlPromise('putObject', params);
    return uploadURL;
}

/*async function getFile() {
    const textName =  'arquivos/invoice.pdf'

    const params = ({
        Bucket: bucketName,
        Key: textName
    });

    const getURL = await s3.getSignedUrlPromise('getObject', params);
    return getURL;
}*/


async function uploadText() {
    const txtName = 'arquivos/j_son.json';

    const params = ({
        Bucket: bucketName,
        Key: txtName,
    });

    const uploadURL2 = await s3.getSignedUrlPromise('putObject', params);
    return uploadURL2;
}


module.exports = { uploadFile, uploadText };