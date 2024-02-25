


var AjaxQueryBase = (function () {

  function getJSON(header) {
    return $.ajax(
      header
    ).done(function (data) {
      return data
    }).fail(function (data) {
      ajax_error(data.responseText, header['url'])
    })
  }

  return {
    info: getJSON
  }
})();

var AjaxQuery = (function () {

  function getJSON(header, done_func) {
    return AjaxQueryBase.info(header).done(function(data) {

        if (data['error']) {
          server_error(data)       
        } else {
          done_func(data)
        }

    })
  }

  // Возврат
  return {
    info: getJSON
  }

})();
