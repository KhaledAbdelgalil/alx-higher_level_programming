$('document').ready(function () {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
    $('INPUT#btn_translate').click(function () {
        const langCode = $('INPUT#language_code').val();
        let full_url = url + langCode;
      $.get(full_url, function (data) {
        $('DIV#hello').html(data.hello);
      });
    });
  });