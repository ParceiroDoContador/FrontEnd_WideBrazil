
const dataForm = document.querySelector('#dataForm');
const dataInput = document.querySelector('#file');
const downInput = document.querySelector('#downInput');
const downForm = document.querySelector('#downForm');



dataForm.addEventListener('submit', async event => {
    event.preventDefault();
    const dataFile = dataInput.files[0];

    const { url } = await fetch('http://localhost:8080/s3Url').then(res => res.json());
    

    await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'multipart/form-data',
        },
        body: dataFile
    });

const dataUrl = url.split('?')[0];
console.log(dataUrl);

});

downInput.addEventListener('submit', async event => {
    event.preventDefault();

    const { url2 } = await fetch('http://localhost:8080/s3UrlGet').then(req => req.json());

    await fetch(url2, {
        method: 'GET',
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    
    const dataUrl2 = url2.split('?')[0];
    console.log(dataUrl2);

});

