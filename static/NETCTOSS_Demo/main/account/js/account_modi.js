var flag1 = true;
var flag2 = true;
var flag3 = true;
var flag4 = true;
var flag5 = true;
var flag6 = true;
var flag7 = true;
var flag8 = true;
var flag9 = true;
var flag10 = true;

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

$('#check_old_pwd').blur(function () {
    var o_pwd = $(this).val();
    if (o_pwd === '') {
        flag2 = true;
        $('#old_pwd_info').html('');
    } else {
        var a_id = $('#account_id').val();
        $.getJSON(
            '/account/check_old_pwd/',
            {'a_id': a_id, 'o_pwd': o_pwd},
            function (data) {
                if (data['flag']) {
                    $('#old_pwd_info').html('');
                    $('#check_new_pwd').removeAttr('disabled');
                    $('#confirm_pwd').removeAttr('disabled');
                    flag2 = true;
                } else {
                    $('#old_pwd_info').html('密码不正确').css('color', 'red');
                    $('#check_new_pwd').attr('disabled', 'disabled');
                    $('#confirm_pwd').attr('disabled', 'disabled');
                    flag2 = false;
                }
            }
        );
    }
});

$('#check_new_pwd').blur(function () {
    var pwd = $(this).val();
    if (pwd === '') {
        flag3 = true;
        $('#new_pwd_info').html('');
    } else {
        $.getJSON(
            '/account/check_pwd/',
            {'pwd': pwd},
            function (data) {
                if (data['flag']) {
                    $('#new_pwd_info').html('');
                    flag3 = true;
                } else {
                    $('#new_pwd_info').html('密码格式不正确').css('color', 'red');
                    flag3 = false;
                }
            }
        );
    }
    if ($('#confirm_pwd').val()) {
        var c_pwd = $('#confirm_pwd').val();
        $.getJSON(
            '/account/confirm_pwd/',
            {'pwd': pwd, 'c_pwd': c_pwd},
            function (data) {
                if (data['flag']) {
                    $('#c_pwd_info').html('');
                    flag4 = true;
                } else {
                    $('#c_pwd_info').html('两次密码不一致').css('color', 'red');
                    flag4 = false;
                }
            })
    }
});

$('#confirm_pwd').blur(function () {
    var pwd = $('#check_pwd').val();
    var c_pwd = $(this).val();
    if (pwd === '' && c_pwd === '') {
        flag4 = true;
        $('#cpwd_info').html('');
    } else {
        $.getJSON(
            '/account/confirm_pwd/',
            {'pwd': pwd, 'c_pwd': c_pwd},
            function (data) {
                if (data['flag']) {
                    $('#cpwd_info').html('');
                    flag4 = true;
                } else {
                    $('#cpwd_info').html('两次密码不一致').css('color', 'red');
                    flag4 = false;
                }
            })
    }
});

$('#check_tel').blur(function () {
    var tel = $(this).val();
    $.getJSON(
        '/account/check_tel/',
        {'tel': tel},
        function (data) {
            if (data['flag']) {
                $('#tel_info').html('');
                flag5 = true;
            } else {
                $('#tel_info').html('电话号码格式不正确').css('color', 'red');
                flag5 = false;
            }
        }
    )

});

$('#check_r_identity').blur(function () {
    var identity = $(this).val();
    if (identity === '') {
        flag6 = true;
        $('#identity_info').html('');
    } else {
        $.getJSON(
            '/account/check_identity/',
            {'identity': identity},
            function (data) {
                if (data['flag']) {
                    $('#identity_info').html('');
                    flag6 = true;
                } else {
                    $('#identity_info').html('身份证号格式不正确').css('color', 'red');
                    flag6 = false;
                }
            }
        )
    }
});

$('#check_email').blur(function () {
    var email = $(this).val();
    if (email === '') {
        flag7 = true;
        $('#email_info').html('');
    } else {
        $.getJSON(
            '/account/check_email/',
            {'email': email},
            function (data) {
                if (data['flag']) {
                    $('#email_info').html('');
                    flag7 = true;
                } else {
                    $('#email_info').html('身份证号格式不正确').css('color', 'red');
                    flag7 = false;
                }
            }
        )
    }
});

$('#check_mailaddress').blur(function () {
    var mailaddress = $(this).val();
    if (mailaddress === '') {
        flag8 = true;
        $('#mailaddress_info').html('');
    } else {
        $.getJSON(
            '/account/check_mailaddress/',
            {'mailaddress': mailaddress},
            function (data) {
                if (data['flag']) {
                    $('#mailaddress_info').html('');
                    flag8 = true;
                } else {
                    $('#mailaddress_info').html('身份证号格式不正确').css('color', 'red');
                    flag8 = false;
                }
            }
        )
    }
});

$('#check_zipcode').blur(function () {
    var zipcode = $(this).val();
    if (zipcode === '') {
        flag9 = true;
        $('#zipcode_info').html('');
    } else {
        $.getJSON(
            '/account/check_zipcode/',
            {'zipcode': zipcode},
            function (data) {
                if (data['flag']) {
                    $('#zipcode_info').html('');
                    flag9 = true;
                } else {
                    $('#zipcode_info').html('身份证号格式不正确').css('color', 'red');
                    flag9 = false;
                }
            }
        )
    }
});

$('#check_qq').blur(function () {
    var qq = $(this).val();
    if (qq === '') {
        flag10 = true;
        $('#qq_info').html('');
    } else {
        $.getJSON(
            '/account/check_qq/',
            {'qq': qq},
            function (data) {
                if (data['flag']) {
                    $('#qq_info').html('');
                    flag10 = true;
                } else {
                    $('#qq_info').html('身份证号格式不正确').css('color', 'red');
                    flag10 = false;
                }
            }
        )
    }
});

//保存成功的提示信息
function save_modification() {
    var flag = flag1 && flag2 && flag3 && flag4 && flag5 && flag6 && flag7 && flag8 && flag9 && flag10;
    if (flag) {
        var a_id = $('#account_id').val();
        var name = $('#check_name').val();
        var pwd = $('#check_pwd').val();
        var tel = $('#check_tel').val();
        var identity = $('#check_r_identity').val();
        var email = $('#check_email').val();
        var mailaddress = $('#check_mailaddress').val();
        var zipcode = $('#check_zipcode').val();
        var qq = $('#check_qq').val();

        if (identity === '') identity = '0';
        if (email === '') email = '0';
        if (mailaddress === '') mailaddress = '0';
        if (zipcode === '') zipcode = '0';
        if (qq === '') qq = '0';

        $.getJSON(
            '/account/save_modifications/',
            {
                'a_id': a_id,
                'name': name,
                'pwd': pwd,
                'tel': tel,
                'identity': identity,
                'email': email,
                'mailaddress': mailaddress,
                'zipcode': zipcode,
                'qq': qq
            },
            function () {

            }
        )
    }

    function showResult() {
        showResultDiv(true);
        window.setTimeout("showResultDiv(false);", 5000);
    }

    function showResultDiv(flag) {
        var divResult = document.getElementById("save_result_info");
        if (flag)
            divResult.style.display = "block";
        else
            divResult.style.display = "none";
    }
}