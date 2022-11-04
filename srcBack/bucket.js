const aws = require('aws-sdk');
const dotEnv = require('dotenv');
const crypto = require('crypto');
const {promisify} = require('util');


const randomName = promisify(crypto.randomBytes);
dotEnv.config();

const region = 'sa-east-1';
const bucketName = 'datafile-direct-bucket'
const accessKeyId = 'AKIA3WLWJHVCI4BRDMXK';
const secretAccessKey = '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';

const s3 = new aws.S3({
    region,
    accessKeyId,
    secretAccessKey,
    signatureVersion: 'v4',
});

 async function uploadFile() {
    const rawBytes = await randomName(16);
    const fileName = rawBytes.toString('hex');

    const params = ({
        Bucket: bucketName,
        Key: fileName,
        Expires: 60
    });

    const uploadURL = await s3.getSignedUrlPromise('putObject', params);
    return uploadURL;
}

module.exports = { uploadFile };