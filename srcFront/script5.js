const dataForm = document.querySelector('#dataForm');
const file = document.querySelector('#file');


file.addEventListener('change', () => {
    let nome = 'Não há arquivo selecionado.'
    if (file.files.length > 0) { 
        nome = file.files[0].name;
    }

    let localStore = localStorage.setItem('InfoFile', nome)
    console.log(localStorage.getItem('InfoFile'))
    //fazer log dos nomes dos arquivos
});

dataForm.addEventListener('submit', async event => {
    event.preventDefault();

    const dataFile = file.files[0];
    const { url } = await fetch('http://localhost:8080/s3Url4').then(res => res.json());

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

