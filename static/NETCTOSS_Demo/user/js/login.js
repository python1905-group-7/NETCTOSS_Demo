$(function () {
    $('body').addClass('index');

     $('#changeImage').click(function () {
         $(this).attr('src', '/login/get_code/?' + Math.random())
     });
})