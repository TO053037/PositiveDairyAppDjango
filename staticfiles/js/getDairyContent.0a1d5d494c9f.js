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
                    console.log(response)
                    console.log('test');
                    document.getElementById('textarea-' + ranking.toString()).value = response.content;
                } else if (response.status === 404) {
                    document.getElementById('textarea-' + ranking.toString()).value = '';
                    console.log(response.message);
                }
            } else {
                console.log('error');
            }
        })
}
