function logar() {
    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;

    let usuario = {
        email: email,
        senha: senha 
    }

    fetch("http://localhost:8080/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(usuario)
    }).then(response => { 
        if (response.status == 200) {
            window.location.href = "http://localhost:3000/page1.html";
        } else {
            alert("Usuário ou senha inválidos");
        }
    }
    )

}
