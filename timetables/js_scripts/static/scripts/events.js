

var main = (function() {

    function _bindHandlers() {

        $('#page_content').on('click.pageNameSpace', '.weekday_num', change_weekday)

        $('#page_content').on('change.pageNameSpace', '.timetable_ceil', save_ceil)
        $('#page_content').on('click.pageNameSpace', '#clear', clear_timetable)
        $('#page_content').on('click.pageNameSpace', '.column_btn', clear_column)
        $('#page_content').on('click.pageNameSpace', '.row_btn', clear_row)

        $('#page_content').on('click.pageNameSpace', '.deactivate', deactivate)
        $('#page_content').on('focusout.pageNameSpace', '.tm_input', change_name)


        $('#page_content').on('click.pageNameSpace', '#zero_division', devide_by_zero)

    }

    function init() {
        _bindHandlers();

    }

      // Возвращаем наружу
    return {
        init: init
    }
})()

$(document).ready(main.init);