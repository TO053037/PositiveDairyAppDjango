function postDairyPicture() {
    const urlLength = postDairyPictureUrl.length;
    let date = document.getElementById('dairy-content-form').className;
    window.location.href = postDairyPictureUrl.replace(postDairyPictureUrl.slice(urlLength - 10, urlLength), date);
}