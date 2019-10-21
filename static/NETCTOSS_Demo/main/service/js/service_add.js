$(function () {
    $('.btn_search_large').click(function () {
        var idcard_No = $(this).prev().val();
        var $btn = $(this);
        $.getJSON(
            '/service/query_idcard_no/',
            {'idcard_No':idcard_No},
            function (data) {
                if (data['status']==200){
                    $btn.next().html(data['msg']);
                }else {
                    $btn.next().html(data['msg']);
                }
            }
        );
    });


    $('#s_query').blur(function () {
        var account_id = $(this).val();
        var $s_query = $(this);
        if (isNaN(account_id)){
            $s_query.next().next().html('账务账号是数字！！');
        }else {
            $.getJSON(
            '/service/account_id_query/',
            {'account_id':account_id},
            function (data) {
                if (data['status']==200){
                    console.log(data['msg']);
                    $s_query.next().next().html(data['msg']);
                }else {
                    $s_query.next().next().html(data['msg']);
                }
            }
        );
        }
    });


        $('#unix_host').blur(function () {
            var unix_host = $(this).val();
            // var re_host = /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/;
            var re_host= /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
            var a = re_host.test(unix_host);
            if (a){
                $(this).next().next().html('ip地址输入正确');
            }else {
                $(this).next().next().html('ip地址输入有误');
            }
        });

        $('#os_account').blur(function () {
            var os_account = $(this).val();
            var re_account = /^[a-zA-Z_0-9]{1,8}$/;
            var p = re_account.test(os_account);
            if (p){
                $(this).next().next().html('格式正确');
            }else {
                $(this).next().next().html('格式不正确');
            }
        });

        $('#password1').blur(function () {
            var password = $(this).val();
            var re_password = /^[a-zA-Z_0-9]{3,32}$/;
            var p = re_password.test(password);
            if (p){
                $(this).next().next().html('格式正确');
            }else {
                $(this).next().next().html('格式不正确');
            }
        });

         $('#password2').blur(function () {
            var password1 = $(this).val();
            var password2 = $(this).parent().prev().prev().find('input').val();

            if (password1 === password2){
                $(this).next().next().html('两次密码一致');
            }else {
                $(this).next().next().html('两次密码不一致');
            }
        });

         $('#save_service').click(function () {
         //    判断身份证号
             alert('123');
             var idcard = $('#idcard_no').val();
             var accountid = $('#s_query').val();
             var unix_host = $('#unix_host').val();
             var os_account = $('#os_account').val();
             var costname = $('#costname').text();
             var password1 = $('#password1').val();
             var password2 = $('#password2').val();

             console.log(idcard,accountid,unix_host,os_account,password1,password2);

             if (idcard && accountid && unix_host && os_account && password1 && password2){
                     var password = md5(password1);
                     console.log(password);
                     $('#password1').val(password);
                     $('#password2').val(password);
                     $.ajax({
                         url:'/service/add_service/',
                         data:{'accountid':accountid,'unix_host':unix_host,'os_account':os_account,'costname':costname,'password':password},
                         type:'POST',
                         dataType:'json',
                         success:function (data) {
                               if (data['status']==200){
                                   location.href='/service/service_list/';
                               }else{
                                             $('#save_result_info').html(data['msg']);
                                             $("#save_result_info").show();
                                            var m = window.setTimeout(function (){$("#save_result_info").hide()},3000);
                                     }
                         }
                     });

             }else {
                     $('#save_result_info').html('请输入完整信息');
                     $("#save_result_info").show();
                    var m = window.setTimeout(function (){$("#save_result_info").hide()},3000);
             }

         });


});