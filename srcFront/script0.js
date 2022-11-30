const email = document.querySelector('#email');
const senha = document.querySelector('#senha');
const infosForms = document.querySelector('#infosForms')

infosForms.addEventListener('submit', async event => {
    event.preventDefault();

    try {
        await fetch('https://wide-brazil-web-app-pd9vq.ondigitalocean.app/srcBack/login',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email.value,
                senha: senha.value
            })
        }).then(resposta => {
            if (resposta.status === 200) {
                resposta.json().then(dados => {
                    localStorage.setItem('token', dados.token)
                    window.location.href = 'http://wide.parceirodocontador.com.br/srcFront/page1.html';
                })
            } else if (resposta.status === 400) {
                alert('Usuário ou senha inválidos');
            }
             });
    } catch (error) {
        console.log(error);
    }      
})

        

























