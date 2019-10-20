var flag1 = false;
var flag2 = false;
var flag3 = false;
var flag4 = false;
var flag5 = false;
var flag6 = false;

$('#check_name').blur(function () {
    var name = $(this).val();
    $.getJSON(
        '/account/check_name/',
        {'name': name},
        function (data) {
            if (data['flag']) {
                $('#name_info').html('');
                flag1 = true;
            } else {
                $('#name_info').html('用户名格式不正确').css('color', 'red');
                flag1 = false;
            }
        }
    )
});

$('#check_identity').blur(function () {
    var identity = $(this).val();
    $.getJSON(
        '/account/check_identity/',
        {'identity': identity},
        function (data) {
            if (data['flag']) {
                $('#identity_info').html('');
                flag2 = true;
            } else {
                $('#identity_info').html('身份证号格式不正确').css('color', 'red');
                flag2 = false;
            }
        }
    )
});

$('#check_account').blur(function () {
    var account = $(this).val();
    $.getJSON(
        '/account/check_account/',
        {'account': account},
        function (data) {
            if (data['flag']) {
                $('#account_info').html('');
                flag3 = true;
            } else {
                $('#account_info').html('账号格式不正确').css('color', 'red');
                flag3 = false;
            }
        }
    )
});

$('#check_pwd').blur(function () {
    var pwd = $(this).val();
    $.getJSON(
        '/account/check_pwd/',
        {'pwd': pwd},
        function (data) {
            if (data['flag']) {
                $('#pwd_info').html('');
                flag4 = true;
            } else {
                $('#pwd_info').html('密码格式不正确').css('color', 'red');
                flag4 = false;
            }
        }
    );
    if ($('#confirm_pwd').val()) {
        var c_pwd = $('#confirm_pwd').val();
        $.getJSON(
            '/account/confirm_pwd/',
            {'pwd': pwd, 'c_pwd': c_pwd},
            function (data) {
                if (data['flag']) {
                    $('#cpwd_info').html('');
                    flag5 = true;
                } else {
                    $('#cpwd_info').html('两次密码不一致').css('color', 'red');
                    flag5 = false;
                }
            })
    }
});


$('#confirm_pwd').blur(function () {
    var pwd = $('#check_pwd').val();
    var c_pwd = $(this).val();
    $.getJSON(
        '/account/confirm_pwd/',
        {'pwd': pwd, 'c_pwd': c_pwd},
        function (data) {
            if (data['flag']) {
                $('#cpwd_info').html('');
                flag5 = true;
            } else {
                $('#cpwd_info').html('两次密码不一致').css('color', 'red');
                flag5 = false;
            }
        })
});

$('#check_tel').blur(function () {
    var tel = $(this).val();
    $.getJSON(
        '/account/check_tel/',
        {'tel': tel},
        function (data) {
            if (data['flag']) {
                $('#tel_info').html('');
                flag6 = true;
            } else {
                $('#tel_info').html('电话号码格式不正确').css('color', 'red');
                flag6 = false;
            }
        }
    )
});

function add_user() {
    if (flag1 && flag2 && flag3 && flag4 && flag5 && flag6) {
        var name = $('#check_name').val();
        var identity = $('#check_identity').val();
        var account = $('#check_account').val();
        var pwd = $('#check_pwd').val();
        var tel = $('#check_tel').val();
        $('#check_pwd').val(md5(pwd));
        $('#confirm_pwd').val(md5(pwd));
        $.getJSON(
            '/account/add_user/',
            {'name': name, 'identity': identity, 'account': account, 'pwd': pwd, 'tel': tel},
            function (data) {

            }
        )
    }
}