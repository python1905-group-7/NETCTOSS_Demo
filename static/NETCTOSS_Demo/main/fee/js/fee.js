$(function () {
    $.get(
        '/login/get_user/',
        {},
        function (data) {
            if (data['status'] === 200) {
                $('#header').find('b').html(data['data']['admin_code']);
            } else {
                console.log(123)
                window.location.href = '/login/'
            }
        }
    )
});