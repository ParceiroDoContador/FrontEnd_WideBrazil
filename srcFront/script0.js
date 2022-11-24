function logar() {
    let email = document.getElementById('email')
    let senha = document.getElementById('senha')

    let dados = {
        email: email.value,
        senha: senha.value
    }

    let cabecalho = {
        method: 'POST',
        body: JSON.stringify(dados),
        headers: {
            'Content-type': 'application/json'
        }
    }
    
    fetch('http://localhost:8080/login', cabecalho)
        .then(resposta => {
            if (resposta.ok) {
                return resposta.json()
            } else {
                throw new Error('Não foi possível fazer login')
            }
        }
        )
        .then(dados => {
            localStorage.setItem('token', dados.token)
            window.location.href = 'http://localhost:3000/srcFront/page1.html'
        }
        )
        .catch(erro => {
            console.log(erro)
        }
        )
}
