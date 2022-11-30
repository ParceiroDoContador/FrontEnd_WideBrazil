const downInput = document.querySelector('#downInput');
const linkRef = document.querySelector('#linkRef');
const nomeCliente = document.querySelector('#nomeCliente');
const valorDolar = document.querySelector('#valorDolar');
const infosForms = document.querySelector('#infosForms');

downInput.addEventListener('click', async event => {
    event.preventDefault();
    const token = localStorage.getItem('token');

    if (!token) {
        alert('Você precisa estar logado para fazer download de arquivos');
        window.location.href = 'http://wide.parceirodocontador.com.br/srcFront/page0.html';
    }
    

   const { url2 } = await fetch('http://localhost:8080/s3UrlGet').then(res => res.json());

    await fetch(url2, {
        method: 'GET',
        headers: {
            'Content-Type': 'aplication/pdf',
        },
    });

    const dataUrl2 = url2.split('?')[0]; 
    console.log(dataUrl2);

    linkRef.href = `${dataUrl2}`;
    linkRef.download = 'planilha_wide.pdf';
    linkRef.target = '_blank';
    linkRef.click();
});

downInput.addEventListener('click', async event => {
    event.preventDefault();
    const token = localStorage.getItem('token');

    if (!token) {
        alert('Você precisa estar logado para fazer download de arquivos');
        window.location.href = 'http://localhost:3000/srcFront/page0.html';
    }

    const nome = document.getElementById('nomeCliente').value;
    const dolar = document.getElementById('valorDolar').value;
    
    const { url3 } = await fetch('http://localhost:8080/s3UrlPut').then(res => res.json());

    await fetch(url3, {
        method: 'PUT',
        headers: {
            'Content-Type': 'aplication/json',
        },
        body: JSON.stringify({ nome, dolar }),
    });

    const dataUrl3 = url3.split('?')[0];
    console.log(dataUrl3);

    nomeCliente.value = '';
    valorDolar.value = '';
});

