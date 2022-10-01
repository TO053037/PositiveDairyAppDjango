function onloadEvent() {
    const date = createNewClass()
    getDairyContent(date, 1)
    getDairyContent(date, 2)
    getDairyContent(date, 3)
}

window.onload = onloadEvent;