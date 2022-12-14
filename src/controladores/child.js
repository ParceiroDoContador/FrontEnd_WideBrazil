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
    const dirname = __dirname
    const pythonPath = `${dirname}/scriptFerias.py`
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
}

async function pythonRunFlash() {
    const dirname = __dirname
    const pythonPath = `${dirname}/scriptFlash.py`
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
}

async function pythonRunSeguro() {
    const dirname = __dirname
    const pythonPath = `${dirname}/scriptSeguro.py`
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
}

async function pythonRunInvoice() {
    const dirname = __dirname
    const pythonPath = `${dirname}/scriptInvoice.py`
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
}

    

module.exports = {
    pythonRunDecimo,
    pythonRunFerias,
    pythonRunFlash,
    pythonRunSeguro,
    pythonRunInvoice
}

