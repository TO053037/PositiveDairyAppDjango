async function getDairyPicture(date) {
    const queryParams = new URLSearchParams({
        'date': date,
    })
    const resJson = await fetch(getDairyPictureUrl + '?' + queryParams);
    const res = await resJson.json()
    console.log(res);
    const showPicturesElement = document.getElementById('show-picture');
    if (res.status === 200) {
        while(showPicturesElement.firstChild) {
            showPicturesElement.removeChild(showPicturesElement.firstChild);
        }
        if (res.pictureUrls.length > 0) {
            console.log(res.pictureUrls);
            for (let i = 0; i < res.pictureUrls.length; i ++) {
                let newElement = document.createElement('img');
                newElement.src = res.pictureUrls[i];
                newElement.height = 200;
                newElement.width = 200;
                showPicturesElement.appendChild(newElement);
            }
        }
    }
}