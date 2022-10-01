function getDairyContent(date, ranking) {
    console.log(date, ranking);
    console.log(typeof date);
    console.log(typeof ranking);
    $.ajax({
        'url': getDairyContentUrl,
        'type': 'GET',
        'data': {
            'date': date,
            'ranking': ranking,
        },
        'dataType': 'json'
    })
        .done(function (response) {
            if (response) {
                if (response.status === 200) {
                    console.log(response)
                    document.getElementById('textarea-' + ranking.toString()).value = response.content;
                }
            } else {
                console.log('error');
            }
        })
}
