const dataForm = document.querySelector('#dataForm');
const file = document.querySelector('#file');


file.addEventListener('change', () => {
    let nome = 'Não há arquivo selecionado.'
    if (file.files.length > 0) { 
        nome = file.files[0].name;
    }

    fetch('http://localhost:8080/log', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome })
    }).then(resposta => { 
        console.log(resposta);
});

dataForm.addEventListener('submit', async event => {
    event.preventDefault();

    const dataFile = file.files[0]

    const { url } = await fetch('http://localhost:8080/s3Url1').then(res => res.json());
   
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









