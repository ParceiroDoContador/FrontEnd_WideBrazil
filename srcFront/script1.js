
const downInput = document.querySelector('#downInput');
const linkRef = document.querySelector('#linkRef');


downInput.addEventListener('click', async event => {
    event.preventDefault();

    const { url2 } = await fetch('http://localhost:8080/s3UrlGet').then(res => res.json());

    await fetch(url2, {
        method: 'GET',
        headers: {
            'Content-Type': 'aplication/pdf',
        },
    });

    const dataUrl2 = url2.split('?')[0]; 
    console.log(dataUrl2);

    linkRef.href = `${dataUrl2}`;
    linkRef.download = 'planilha_wide.pdf';
    linkRef.target = '_blank';
    linkRef.click();

});