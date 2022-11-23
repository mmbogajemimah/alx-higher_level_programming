$(function () {
  // Select the element to be clicked and bind it with the click listener
  $('#red_header').bind('click', function () {
    // On clicking the element add a class to the header element
    $('header').addClass('red');
  });
});
