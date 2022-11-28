// JQUERY
$(function () {
  // When the btn_translate is clicke
  // The value in the input is taken in and concatnated with the API
  // The API gets us back the data=> a promise which has the interpration of the language (Hello)
  $('#btn_translate').bind('click', function () {
    const language = $('#language_code').val();
    // console.log(language)
    $.get('https://stefanbohacek.com/hellosalut/?lang=' + language,
      function (data) {
        $('#hello').text(data.hello);
      });
  });

  // I want the translate button to be pressed when I click on the enter button
  // If The input button is on focus when the enter key is pressed
  // The value in the input is taken in and concatnated with the API
  // The API gets us back the data=> a promise which has the interpration of the language (Hello)
  $('#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      const lang = $('#language_code').val();
      // console.log(lang)
      $.get('https://stefanbohacek.com/hellosalut/?lang=' + lang,
        function (data) {
          $('#hello').text(data.hello);
        });
    }
  });
});
