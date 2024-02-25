

var error = (function () {

    function onCatchError(response) {
          // var json = response.responseJSON,
          //   message = (json && json.error)
          //     ? json.error
          //     : json['text_error'];
    }
  
     // Привязка событий
     function _bindHandlers() {
  
        $('#error_modal').on('click.error_modal', '#error_info', show_error_info)
        $('#error_modal').on('click.error_modal', '#error_close', hide_error_info)

    }
  
  
  
    // Инициализация приложения
    function init() {
      _bindHandlers();
  
    }
  
    // Возвращаем наружу
    return {
      onCatchError: onCatchError,
      init: init
    }
  })();

  // Запускаем приложение диалоговое тестирование
  $(document).ready(error.init);