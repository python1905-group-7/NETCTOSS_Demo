$('.real_name').click(function () {
    var real_name = $(this).html();
    $.getJSON(
        '/account/find_name/',
        {'real_name': real_name},
        function () {
            location.href = '/account/account_detail/'
        }
    )
});

$('.btn_modify').click(function () {
    var real_name = $(this).parent().parent().children().eq(1).html();
    $.getJSON(
        '/account/find_name/',
        {'real_name': real_name},
        function () {
            location.href = '/account/account_modi/'
        }
    )
});