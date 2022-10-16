function onloadEvent() {
    const date = createNewClass()
    getDairyContent(date, 1);
    getDairyContent(date, 2);
    getDairyContent(date, 3);
    getDairyPicture(date);
}

window.onload = onloadEvent;