const email = document.querySelector('#email');
const senha = document.querySelector('#senha');
const infosForms = document.querySelector('#infosForms')

infosForms.addEventListener('submit', async event => {
    event.preventDefault();
    
        await fetch('/login', {
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



























/*function logar() {
    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;

    let dados = {
        email: email,
        senha: senha
    }
    localStorage.setItem("dados", JSON.stringify(dados));
    console.log(dados);
    if (!email || !senha) {
        alert('Preencha todos os campos!')
    }

    let cabecalho = {
        method: 'POST',
        body: JSON.stringify(dados),
        headers: {
            'Content-type': 'application/json'
        }
    }
    
    fetch('http://localhost:8080/srcBack/login', cabecalho)
        .then(dados => {
            localStorage.setItem('token', dados.token)
            window.location.href = 'http://localhost:3000/srcFront/page1.html'
        }
        )
        .catch(erro => {
            console.log(erro)
        }
    )
}*/
})
