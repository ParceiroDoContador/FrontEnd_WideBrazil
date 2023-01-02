const downInput = document.querySelector('#downInput');
const linkRef = document.querySelector('#linkRef');
const nomeCliente = document.querySelector('#nomeCliente');
const valorDolar = document.querySelector('#valorDolar');
const infosForms = document.querySelector('#infosForms');
const urlServer = 'https://wide.parceirodocontador.com.br'


/*async function downloadInvoice() {
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
        linkRef.download = 'arquivos/invoice.pdf';
        linkRef.target = '_blank';
        linkRef.click();
    
} catch (error) {
    console.log(error);
}
}*/

downInput.addEventListener('click', async event => {
    event.preventDefault();
    const token = localStorage.getItem('token');

    if (!token) {
        alert('Você precisa estar logado para fazer download de arquivos');
        window.location.href = `${urlServer}/static/page0.html`;
    }
    
    const nome = document.getElementById('nomeCliente').value;
    const cotacao_dolar = document.getElementById('valorDolar').value;


    if (nome === '' || cotacao_dolar === '') {
        alert('Preencha todos os campos');
        return;
    }

    /*let isFloat = cotacao_dolar % 1 === 0

    //if (isFloat) {
    //   alert('O valor do dolar deve conter apenas números e as casas decimais separadas por ponto');
    // return;
     }*/


    const { url3 } = await fetch(`${urlServer}/s3UrlPut`, {
        headers: {
            authorization: token
        }
    }).then(res => res.json());

    await fetch(url3, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome, cotacao_dolar })
    }).then(resposta => {})

    const dataUrl3 = url3.split('?')[0];
    console.log(dataUrl3);

    await fetch(`${urlServer}/gerarInvoice`, {
        headers: {
            authorization: token
        }
    }).then(res => {
        console.log(res)
        alert('Requisição feita com sucesso!')
    })

    nomeCliente.value = '';
    valorDolar.value = '';


    });

    

