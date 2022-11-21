function splitDate(date) {
    const dateSplit = date.split('-');
    return {
        'year': parseInt(dateSplit[0]),
        'month': parseInt(dateSplit[1]),
        'day': parseInt(dateSplit[2]),
    }
}