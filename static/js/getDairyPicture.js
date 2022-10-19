async function getDairyPicture(date) {
    const queryParams = new URLSearchParams({
        'date': date,
    })
    const resJson = await fetch(getDairyPictureUrl + '?' + queryParams);
    const res = await resJson.json()
    console.log(res);
    const showPicturesElement = document.getElementById('show-picture-ul');
    if (res.status === 200) {
        while(showPicturesElement.firstChild) {
            showPicturesElement.removeChild(showPicturesElement.firstChild);
        }
        if (res.pictureUrls.length > 0) {
            console.log(res.pictureUrls);
            for (let i = 0; i < res.pictureUrls.length; i ++) {
                let imgElement = document.createElement('img');
                let liElement = document.createElement('li');
                liElement.classList.add('p-2.5');
                imgElement.src = res.pictureUrls[i]
                imgElement.height = 200;
                imgElement.width = 200;
                liElement.appendChild(imgElement)
                showPicturesElement.appendChild(liElement)
                console.log('test');
            }
        }
    }
}