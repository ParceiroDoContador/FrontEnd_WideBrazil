const email = document.querySelector('#email');
const senha = document.querySelector('#senha');
const infosForms = document.querySelector('#infosForms')
const urlServer = 'https://wide.parceirodocontador.com.br'

infosForms.addEventListener('submit', async event => {
    event.preventDefault();

    try {
        await fetch(`${urlServer}/login`,{
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
                    window.location.href = `${urlServer}/static/page1.html`;
                })
            } else if (resposta.status === 400) {
                alert('Usuário ou senha inválidos');
            }
             });
    } catch (error) {
        console.log(error);
    }      
})

        

























