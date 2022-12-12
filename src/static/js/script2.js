const dataForm = document.querySelector('#dataForm');
const file = document.querySelector('#file');
const urlServer = 'https://wide.parceirodocontador.com.br'

file.addEventListener('change', () => {
    let nome = 'Não há arquivo selecionado.'
    if (file.files.length > 0) { 
        nome = file.files[0].name;
    }

    fetch(`${urlServer}/log`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome })
    }).then(resposta => {})

});

dataForm.addEventListener('submit', async event => {
    event.preventDefault();
    const token = localStorage.getItem('token');

    if (!token) {
        alert('Você precisa estar logado para fazer upload de arquivos');
        window.location.href = `${urlServer}/static/page0.html`;
    }

    const dataFile = file.files[0]
    const { url } = await fetch(`${urlServer}/upload-url?folderNumber=1`, {
    headers: {
    authorization: token
    }}).then(res => res.json());

   await fetch(url, {
       method: 'PUT',
       headers: {
            'Content-Type': 'multipart/form-data',
      },
       body: dataFile
   });
      const dataUrl = url.split('?')[0];
      console.log(dataUrl);
      alert('Arquivo enviado com sucesso!');

    await fetch('https://starfish-app-48vqf.ondigitalocean.app/upload-ferias', {mode:'no-cors'}).then(res => {
        console.log(res);
    })


});

