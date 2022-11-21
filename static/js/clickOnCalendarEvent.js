function clickOnCalendarEvent(date) {
    console.log('staticfiles');
    getDairyContent(date, 1);
    getDairyContent(date, 2);
    getDairyContent(date, 3);
    console.log(getDairyPicture(date));
    addClassDate(date);
    show_selected_date(date);

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

function show_selected_date(date) {
    console.log('in func');
    document.getElementById('show-date').innerHTML = date;
}

