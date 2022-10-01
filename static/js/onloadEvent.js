function getDairyContentToday() {
    const date = createNewClass()
    getDairyContent(date, 1)
    getDairyContent(date, 2)
    getDairyContent(date, 3)
}

function onloadEvent() {
    console.log('in first onload');
    onloadEvent();
    console.log('in onloadEvent');
    getDairyContentToday();
}

window.onload = onloadEvent;