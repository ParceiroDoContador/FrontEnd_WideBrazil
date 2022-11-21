const dataForm = document.querySelector('#dataForm');
const file = document.querySelector('#file');



dataForm.addEventListener('submit', async event => {
    event.preventDefault();


    const { url } = await fetch('http://localhost:8080/s3Url').then(res => res.json());
   
   await fetch(url, {
       method: 'PUT',
       headers: {
            'Content-Type': 'multipart/form-data',
      },
       body: dataFile
   });

      const dataUrl = url.split('?')[0];
      console.log(dataUrl);

});









