function clickOnCalendarEvent(date) {
    getDairyContent(date, 1);
    getDairyContent(date, 2);
    getDairyContent(date, 3);
    addClassDate(date);
}

function createNewClass() {
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    let yyyy = today.getFullYear();
    return yyyy + '-' + mm + '-' + dd;
}

function addClassDate(date) {
    document.getElementById('dairy-content-form').className = date;
}

