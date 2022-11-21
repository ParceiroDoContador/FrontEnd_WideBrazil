const dataForm = document.querySelector('#dataForm');
const file = document.querySelector('#file');
import { fileName } from '../srcBack/bucket.js';


dataForm.addEventListener('submit', async event => {
    event.preventDefault();

    const dataFile = file.files[0];

    const { url } = await fetch('http://localhost:8080/s3Url').then(res => res.json());
    fileName = `import2/${dataFile.name}`;


   await fetch(url, {
       method: 'PUT',
       headers: {
            'Content-Type': 'multipart/form-data',
      },
      key: 'import2/planilha_wide.pdf',
       body: dataFile
   });

      const dataUrl = url.split('?')[0];
      console.log(dataUrl);

});
