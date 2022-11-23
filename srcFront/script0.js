function logar() {
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;

    console.log(JSON.stringify({
        email,
        senha
    }));

    fetch('/login', {
        method: 'POST',
        body: JSON.stringify({
                email,
                senha
            }),

        headers: {
            'Content-Type': 'application/json',
        },
        
}).then(async (res)=>{
    let status = await res.text();
    console.log(status);
    if(status == 'conectado') {
        window.location.href = './page1.html';
    } else {
        alert('Login ou senha incorretos');
    }

})
}
