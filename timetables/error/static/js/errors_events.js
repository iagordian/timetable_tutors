

// Вызов модального окна с текстом ошибки
function show_error(banner, text, error_text, func_label) {

    if (error_text) {
        $('#error_info').removeAttr('hidden')
        $('#error_text').empty().append(error_text)

        if (func_label) {
            $('#func_name').empty().append(func_label)
        }

    } else {
        $('#error_info').attr('hidden', 'hidden')
    }

    $('#error_human_text').empty().append(text)
    $('#error_banner').empty().append(banner)
    $("#error_modal").modal('show');
}

// Вызов функции show_error со стороны сервера
function server_error(data) {

    if (data['error_text']) {
        data['error_text'] = 'Текст ошибки: ' + data['error_text']
    }
    if (data['func_name']) {
        data['func_name'] = 'Название функции: ' + data['func_name']
    }

    show_error(data['error_banner'], data['error_human_text'], data['error_text'], data['func_name'])
}

// Вызов функции show_error при ошибке ajax-запроса
function ajax_error(response, url) {

    response = 'Ответ сервера: ' + response
    url = 'URL запроса: ' + url

    show_error('Ошибка при запросе к серверу', 'При выполнении AJAX зпроса произошла ошибка',
                response, url)
}

// Вызов функции show_error со стороны клиента
function client_error(banner, text) {
    show_error(banner, text)
}

// Раскрытие пространства подробностей в окне ошибки
function show_error_info() {

    var state = Number($(this).attr('state'))
    $('#error_info_container').slideToggle('slow')
    // Сохраняем состояние области ошибок, чтобы свернуть ее
    // при закрытии окна, если потребуется
    $(this).attr('state', 1 - state)

}

// Сворачивание пространства подробностей ошибок 
// при закрытии окна
function hide_error_info() {

    var state = Number($('#error_info').attr('state'))
    if (state == 1){
        $('#error_info_container').slideToggle('slow')
        $('#error_info').attr('state', 0)
    }
    
}