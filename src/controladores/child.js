//coding=utf-8
const { spawn, exec } = require('child_process')


async function pythonRunDecimo() {
    const pythonScript = '/src/controladores/scriptDecimo.py';
    
    exec(`python ${pythonScript}`, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return;
      }
    
      console.log(`stdout: ${stdout}`);
      console.error(`stderr: ${stderr}`);
    });
    
};

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

