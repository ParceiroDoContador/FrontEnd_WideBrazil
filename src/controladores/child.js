const { spawn } = require('child_process')


async function pythonRunDecimo() {
    let r = "r"
const childPython = spawn('python', [`${r}./src/controladores/scriptDecimo.py`])

childPython.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`)
})

childPython.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`)
})
}

async function pythonRunFerias() {
    const childPython = spawn('python', ['./scriptFerias.py'])
    
    childPython.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`)
    })
    
    childPython.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`)
    })
}

async function pythonRunFlash() {
    const childPython = spawn('python', ['scriptFlash.py'])
    
    childPython.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`)
    })
    
    childPython.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`)
    })
}

async function pythonRunSeguro() {
    const childPython = spawn('python', ['scriptSeguro.py'])
    
    childPython.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`)
    })
    
    childPython.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`)
    })
}

async function pythonRunInvoice() {
    const childPython = spawn('python', ['scriptInvoice.py'])
    
    childPython.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`)
    })
    
    childPython.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`)
    })
}

    

module.exports = {
    pythonRunDecimo,
    pythonRunFerias,
    pythonRunFlash,
    pythonRunSeguro,
    pythonRunInvoice
}

