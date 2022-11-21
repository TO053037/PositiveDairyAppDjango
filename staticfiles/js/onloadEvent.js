function onloadEvent() {
    console.log('in onload func');
    const date = createNewClass()
    getDairyContent(date, 1);
    getDairyContent(date, 2);
    getDairyContent(date, 3);
    getDairyPicture(date);
    document.getElementById('show-date').innerHTML = date;
    
}

window.onload = onloadEvent;