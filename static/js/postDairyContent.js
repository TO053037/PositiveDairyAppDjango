function postDairyContent(ranking) {
    console.log('in post dairy content');


    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    console.log(ranking);
    let date = document.getElementById('dairy-content-form').className;
    console.log(date);
    let content = document.getElementById('textarea-' + ranking.toString()).value;
    console.log(content);
    $.ajax({
        'url': postDairyContentUrl,
        'type': 'POST',
        'data': {
            'date': date,
            'content': content,
            'ranking': ranking,
        },
        'dataType': 'json'
    })
        .done(function (response) {
            console.log('OK');
        })
}