function createNewClass(ranking) {
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    let yyyy = today.getFullYear();
    return yyyy + '-' + mm + '-' + dd;

}

function addClassTodayOnload() {
    console.log('exchange id');
    document.getElementById('dairy-content-form').className = createNewClass()
}

window.onload = addClassTodayOnload;