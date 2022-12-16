const dataForm = document.querySelector('#dataForm');
const file = document.querySelector('#file');
const labelFile = document.querySelector('#labelFile')
const urlServer = 'https://wide.parceirodocontador.com.br'

function mudarInput() {
    const labelFile = document.querySelector('#labelFile');
    const file = document.querySelector('#file');

    nome = file.files[0].name

    labelFile.style.backgroundColor = '#5b5e5d';
    labelFile.textContent = nome
}

function limparInput() {
    const fileInput = document.getElementById('file').value
    const labelFile = document.getElementById('labelFile').value

    fileInput.value = ''
    labelFile.value = ''
}

file.addEventListener('change', () => {
    let nome = 'Não há arquivo selecionado.'
    if (file.files.length > 0) { 
        nome = file.files[0].name;
        mudarInput()
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
    const { url } = await fetch(`${urlServer}/upload-url?folderNumber=3`, {
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
      limparInput()
});
