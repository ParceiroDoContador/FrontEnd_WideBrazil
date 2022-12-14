//coding=utf-8
const { spawn, execFile, exec } = require('child_process')


async function pythonRunDecimo() {
    const dirname = __dirname
    const pythonPath = `${dirname}/scriptDecimo.py`
    console.log(pythonPath);

exec(`python ${pythonPath}`, (error, stdout, stderr) => {
  if (error) {
    console.error(`error: ${error.message}`);
    return;
  }

  if (stderr) {
    console.error(`stderr: ${stderr}`);
    return;
  }

  console.log(`stdout:\n${stdout}`);
});
};

async function pythonRunFerias() {
    const childPython = spawn('python', ['apps@frontend-widebrazil-7d58788955-bmntm:~/src/controladores/scriptFerias.py'])
    
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

