

var help = (function() {

    function _bindHandlers() {

        $('#page_content').on('click.pageNameSpace', '#help', help)

    }

    function init() {
        _bindHandlers();

    }

      // Возвращаем наружу
    return {
        init: init
    }
})()

$(document).ready(help.init);