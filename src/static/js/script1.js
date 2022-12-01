const downInput = document.querySelector('#downInput');
const linkRef = document.querySelector('#linkRef');
const nomeCliente = document.querySelector('#nomeCliente');
const valorDolar = document.querySelector('#valorDolar');
const infosForms = document.querySelector('#infosForms');
const urlServer = 'https://wide.parceirodocontador.com.br'

downInput.addEventListener('click', async event => {
    event.preventDefault();
    const token = localStorage.getItem('token');

    if (!token) {
        alert('Você precisa estar logado para fazer download de arquivos');
        window.location.href = `${urlServer}/static/page0.html`;
    }
    
    const nome = document.getElementById('nomeCliente').value;
    const dolar = document.getElementById('valorDolar').value;
    
    const { url3 } = await fetch(`${urlServer}/s3UrlPut`, {
        headers: {
            authorization: token
        }
    }).then(res => res.json());

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

    linkRef.href = `${dataUrl3}`;
    linkRef.download = 'planilha_wide.pdf';
    linkRef.target = '_blank';
    linkRef.click();
});
