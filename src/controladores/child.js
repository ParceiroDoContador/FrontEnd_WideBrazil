//coding=utf-8
const { spawn } = require('child_process')
const { Buffer } = require('buffer')


async function pythonRunDecimo() {
    const caminhoPython = './src/controladores/scriptDecimo.py'
    const caminhoPythonEncode = Buffer.from(caminhoPython, 'utf8')
const childPython = spawn('python', [`${caminhoPythonEncode}`])

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

