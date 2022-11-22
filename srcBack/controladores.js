const {uploadFile, getFile, uploadText} = require('./bucket')

const fazerUpload1 = async (req, res) => {
    try {
        const url = await uploadFile('import1/','planilha_teste.pdf');
    res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }
}

const fazerUpload2 = async (req, res) => {
    try {
        const url = await uploadFile('Import2/','nome_valor.json');
    res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }
}

const fazerUpload3 = async (req, res) => {
    try {
        const url = await uploadFile('Import3/','nome_valor.json');
    res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }
}

const fazerUpload4 = async (req, res) => {
    try {
        const url = await uploadFile('Import4/','nome_valor.json');
    res.status(200).send({ url });
    } catch (error) {
        console.log(error);
        return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
    }       
}

const fazerDownload = async (req, res) => {
        try {
            const url2 = await getFile();
        res.status(200).send({ url2 });
        } catch (error) {
            console.log(error);
            return res.status(400).send({ error: 'Erro ao fazer download do arquivo' });
        }
    }

const fazerUploadTexto = async (req, res) => {
        try {
            const url3 = await uploadText();
            res.status(200).send({ url3 });
            } catch (error) {
                console.log(error);
                return res.status(400).send({ error: 'Erro ao fazer upload do arquivo' });
            }
}

module.exports = { fazerUpload1,fazerUpload2,fazerUpload3,fazerUpload4,fazerDownload, fazerUploadTexto }