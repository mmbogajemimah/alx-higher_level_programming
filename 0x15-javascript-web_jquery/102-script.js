// JQUERY
$(function () {
  $('#btn_translate').bind('click', function () {
    const language = $('#language_code').val();
    // console.log(language)
    $.get('https://stefanbohacek.com/hellosalut/?lang=' + language,
      function (data) {
        $('#hello').text(data.hello);
      });
  });
});
