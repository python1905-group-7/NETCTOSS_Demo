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
                $('#name_info').html('姓名格式不正确').css('color', 'red');
                flag1 = false;
            }
        }
    );
});


$('#old_pwd').blur(function () {
    var o_pwd = $(this).val();
    if (o_pwd !== '') {
        var account_id = $('#account_id').val();
        $.getJSON(
            '/account/check_old_pwd/',
            {'account_id': account_id, 'o_pwd': o_pwd},
            function (data) {
                if (data['flag']) {
                    $('#old_pwd_info').html('');
                    $('#new_pwd').removeAttr('disabled');
                    $('#confirm_pwd').removeAttr('disabled');
                    flag2 = true;
                } else {
                    $('#old_pwd_info').html('密码不正确').css('color', 'red');
                    $('#new_pwd').attr('disabled', 'disabled');
                    $('#confirm_pwd').attr('disabled', 'disabled');
                    flag2 = false;
                }
            }
        )
    } else {
        $('#old_pwd_info').html('');
        $('#new_pwd').attr('disabled', 'disabled');
        $('#confirm_pwd').attr('disabled', 'disabled');
        flag2 = true;
    }
});

$('#new_pwd').blur(function () {
    var pwd = $(this).val();
    if (pwd !== '') {
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
    } else {
        flag3 = true;
        $('#new_pwd_info').html('');
    }
    if ($('#confirm_pwd').val()) {
        var c_pwd = $('#confirm_pwd').val();
        $.getJSON(
            '/account/confirm_pwd/',
            {'pwd': pwd, 'c_pwd': c_pwd},
            function (data) {
                if (data['flag']) {
                    $('#confirm_pwd_info').html('');
                    flag4 = true;
                } else {
                    $('#confirm_pwd_info').html('两次密码不一致').css('color', 'red');
                    flag4 = false;
                }
            })
    }
});


$('#confirm_pwd').blur(function () {
    var pwd = $('#new_pwd').val();
    var c_pwd = $(this).val();
    if (pwd === '' && c_pwd === '') {
        flag4 = true;
        $('#confirm_pwd_info').html('');
    } else {
        $.getJSON(
            '/account/confirm_pwd/',
            {'pwd': pwd, 'c_pwd': c_pwd},
            function (data) {
                if (data['flag']) {
                    $('#confirm_pwd_info').html('');
                    flag4 = true;
                } else {
                    $('#confirm_pwd_info').html('两次密码不一致').css('color', 'red');
                    flag4 = false;
                }
            });
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
    );
});

$('#check_r_identity').blur(function () {
    var identity = $(this).val();
    if (identity !== '') {
        $.getJSON(
            '/account/check_identity/',
            {'identity': identity},
            function (data) {
                if (data['flag']) {
                    $('#r_identity_info').html('');
                    flag6 = true;
                } else {
                    $('#r_identity_info').html('身份证号格式不正确').css('color', 'red');
                    flag6 = false;
                }
            }
        );
    } else {
        flag6 = true;
        $('#r_identity_info').html('');
    }
});

$('#check_email').blur(function () {
    var email = $(this).val();
    if (email !== '') {
        $.getJSON(
            '/account/check_email/',
            {'email': email},
            function (data) {
                if (data['flag']) {
                    $('#email_info').html('');
                    flag7 = true;
                } else {
                    $('#email_info').html('邮箱格式不正确').css('color', 'red');
                    flag7 = false;
                }
            }
        );
    } else {
        flag7 = true;
        $('#email_info').html('');
    }
});

$('#check_mailaddress').blur(function () {
    var mailaddress = $(this).val();
    if (mailaddress !== '') {
        $.getJSON(
            '/account/check_mailaddress/',
            {'mailaddress': mailaddress},
            function (data) {
                if (data['flag']) {
                    $('#mailaddress_info').html('');
                    flag8 = true;
                } else {
                    $('#mailaddress_info').html('通信地址格式不正确').css('color', 'red');
                    flag8 = false;
                }
            }
        );
    } else {
        flag8 = true;
        $('#mailaddress_info').html('');
    }
});

$('#check_zipcode').blur(function () {
    var zipcode = $(this).val();
    if (zipcode !== '') {
        $.getJSON(
            '/account/check_zipcode/',
            {'zipcode': zipcode},
            function (data) {
                if (data['flag']) {
                    $('#zipcode_info').html('');
                    flag9 = true;
                } else {
                    $('#zipcode_info').html('邮编格式不正确').css('color', 'red');
                    flag9 = false;
                }
            }
        );
    } else {
        flag9 = true;
        $('#zipcode_info').html('');
    }
});

$('#check_qq').blur(function () {
    var qq = $(this).val();
    if (qq !== '') {
        $.getJSON(
            '/account/check_qq/',
            {'qq': qq},
            function (data) {
                if (data['flag']) {
                    $('#qq_info').html('');
                    flag10 = true;
                } else {
                    $('#qq_info').html('QQ格式不正确').css('color', 'red');
                    flag10 = false;
                }
            }
        );
    } else {
        flag10 = true;
        $('#qq_info').html('');
    }
});

//保存成功的提示信息
function showResult() {
    var flag = flag1 && flag2 && flag3 && flag4 && flag5 && flag6 && flag7 && flag8 && flag9 && flag10;
    if (flag) {
        var a_id = $('#account_id').val();
        var name = $('#check_name').val();
        var tel = $('#check_tel').val();
        var r_identity = $('#check_r_identity').val();
        var email = $('#check_email').val();
        var mailaddress = $('#check_mailaddress').val();
        var zipcode = $('#check_zipcode').val();
        var qq = $('#check_qq').val();
        if (r_identity === '') r_identity = '0';
        if (email === '') email = '0';
        if (mailaddress === '') mailaddress = '0';
        if (zipcode === '') zipcode = '0';
        if (qq === '') qq = '0';
        $.getJSON(
            '/account/modify_user/',
            {
                'account_id': a_id,
                'name': name,
                'tel': tel,
                'r_identity': r_identity,
                'email': email,
                'mailaddress': mailaddress,
                'zipcode': zipcode,
                'qq': qq
            },
            function (data) {
                location.href = '/account/account_list/'
            }
        )
    } else {
        showResultDiv(true);
        window.setTimeout("showResultDiv(false);", 5000);
    }
}

function showResultDiv(flag) {
    var divResult = document.getElementById("save_result_info");
    if (flag)
        divResult.style.display = "block";
    else
        divResult.style.display = "none";
}