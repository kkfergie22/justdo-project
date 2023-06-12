$(document).ready(function () {
  // Activate the Bootstrap tabs
  $('#ex1 a[data-mdb-toggle="pill"]').on('click', function (e) {
    e.preventDefault();
    $(this).tab('show');
  });

  // Handle the "Register" button click event
  $('#index-register-btn').on('click', function (e) {
    e.preventDefault();
    $('#ex1 a[href="#pills-register"]').tab('show');
  });
  // Handle the "not a member Register link" button click event
  $('#register-link').on('click', function (e) {
    e.preventDefault();
    $('#ex1 a[href="#pills-register"]').tab('show');
  });

  // Handle the "Login" button click event
  $('#index-login-btn').on('click', function (e) {
    e.preventDefault();
    $('#ex1 a[href="#pills-login"]').tab('show');
  });

  // Handle the "Get Started" button click event
  $('#get-started-btn').on('click', function (e) {
    e.preventDefault();
    $('#ex1 a[href="#pills-register"]').tab('show');
  });
});
