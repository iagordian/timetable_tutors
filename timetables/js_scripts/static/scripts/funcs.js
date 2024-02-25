
// Запрос к серверу на переключение дня недели
function change_weekday() {

    if ($(this).hasClass('active')) {
        return
    }

    var weekday_num = $(this).val()

    var header = {
        'url': '/change_weekday/' + weekday_num,
        'method': 'get'
    }
    AjaxQuery.info(header, function(server_data) {
        $('#title').empty().append(server_data['weekday_title'])
        $('#timetable').empty().append(server_data['timetable'])
    })

    $('.weekday_num').removeClass('active')
    $(this).addClass('active')
}

// Запрос к серверу на сохранение ячейки расписания
function save_ceil() {

    var student_id = $(this).val()
    var lesson_num = $(this).attr('number')
    var tutor_id = $(this).closest('tr').attr('tutor_id')

    var header = {
        'url': '/save_ceil',
        'method': 'post',
        'data': {
            student_id: student_id,
            lesson_num: lesson_num,
            tutor_id: tutor_id
        }
    }
    AjaxQuery.info(header, function(server_data) {})

}

// Запрос к серверу на отключение тьютора или студента
function deactivate() {

    var btn = $(this)
    var active = 1 - Number(btn.attr('active'))
    var person_id = btn.val()
    var person_type = btn.attr('type')


    var header = {
        'url': '/deactivate',
        'method': 'post',
        'data': {
            active: active,
            person_id: person_id,
            person_type: person_type
        }
    }
    AjaxQuery.info(header, function(server_data) {
        $('#timetable').empty().append(server_data['timetable'])

        btn.attr('active', active)
        btn.empty()

        if (active == 1) {
            btn.append('✓')
        }

    })

}

// Запрос к серверу на очистку расписания
function clear_timetable() {

    var header = {
        'url': '/clear_timetable',
        'method': 'get'
    }
    AjaxQuery.info(header, function(server_data) {
        $('#timetable').empty().append(server_data['timetable'])
    })
}

// Запрос к серверу на очистку колонки расписания
function clear_column() {

    var lesson_num = $(this).val()

    var header = {
        'url': '/clear_column/' + lesson_num,
        'method': 'get'
    }
    AjaxQuery.info(header, function(server_data) {
        $('#timetable').empty().append(server_data['timetable'])
    })
}

// Запрос к серверу на очистку строки расписания
function clear_row() {

    var tutor_id = $(this).val()

    var header = {
        'url': '/clear_row/' + tutor_id,
        'method': 'get'
    }
    AjaxQuery.info(header, function(server_data) {
        $('#timetable').empty().append(server_data['timetable'])
    })
}

// Запрос к серверу на изменение имени тьютора или студента
function change_name() {

    var person_type = $(this).attr('type')
    var new_name = $(this).val()
    var person_id = $(this).attr('person_id')

    var header = {
        'url': '/change_name',
        'method': 'post',
        'data': {
            name: new_name,
            person_id: person_id,
            person_type: person_type
        }
    }
    AjaxQuery.info(header, function(server_data) {
        $('.' + server_data['person_id']).empty().append(server_data['new_name'])
    })

}

// Запрос к серверу на попытку деления на 0
function devide_by_zero() {
    var header = {
        'url': '/devision_by_zero',
        'method': 'get'
    }
    AjaxQuery.info(header, function(server_data) {
        alert('Успешно')
    })
}