$(document).ready(() => {
    $('INPUT#btn_translate').click(() => hello_translate());
    $(document).on('keypress', function (e) {
      if (e.which == 13) { hello_translate(); }
    });
  });

function hello_translate() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    const langCode = $('INPUT#language_code').val();
    let full_url = url + langCode;
  $.get(full_url, function (data) {
    $('DIV#hello').html(data.hello);
  });
}