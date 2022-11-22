function getDairyContent(date, ranking) {
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
                    document.getElementById('textarea-' + ranking.toString()).value = response.content;
                } else if (response.status === 404) {
                    document.getElementById('textarea-' + ranking.toString()).value = '';
                }
            } else {
                console.log('error');
            }
        })
}
