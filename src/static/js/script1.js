const downInput = document.querySelector('#downInput');
const linkRef = document.querySelector('#linkRef');
const nomeCliente = document.querySelector('#nomeCliente');
const valorDolar = document.querySelector('#valorDolar');
const infosForms = document.querySelector('#infosForms');
const urlServer = 'https://wide.parceirodocontador.com.br'


async function downloadInvoice() {
    const token = localStorage.getItem('token');

try {
    const { url2 } = await fetch(`${urlServer}/s3UrlGet`, {
        headers: {
            authorization: token
        }
       }).then(res => res.json());
    
        await fetch(url2, {
            method: 'GET',
            headers: {
                'Content-Type': 'aplication/pdf',
            },
        });
    
        const dataUrl2 = url2.split('?')[0]; 
        console.log(dataUrl2);
    
        linkRef.href = `${dataUrl2}`;
        linkRef.download = 'invoice.pdf';
        linkRef.target = '_blank';
        linkRef.click();
    
} catch (error) {
    console.log(error);
}
}

downInput.addEventListener('click', async event => {
    event.preventDefault();
    const token = localStorage.getItem('token');

    if (!token) {
        alert('Você precisa estar logado para fazer download de arquivos');
        window.location.href = `${urlServer}/static/page0.html`;
    }
    
    const nome = document.getElementById('nomeCliente').value;
    const cotacao_dolar = document.getElementById('valorDolar').value;

    /*const {url3} = await fetch(`${urlServer}/s3UrlPut`, {
        headers: {
            authorization: token
        }
    })

    await fetch(url3, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome, cotacao_dolar })
    }).then(resposta => {})*/
        
    await fetch('https://eof0s61ih3lbarl.m.pipedream.net/').then(resposta => {
        if(resposta.body === true) {
            downloadInvoice();
        } else {
            alert('Erro ao rodar o script');
        }
    })

    nomeCliente.value = '';
    valorDolar.value = '';

})
