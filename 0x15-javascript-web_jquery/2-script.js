$(function () {
  // Select the element to be clicked
  $('#red_header').bind('click', function () {
    // On clicking rhe element change the header color to red
    $('header').css('color', '#FF0000');
  });
});
