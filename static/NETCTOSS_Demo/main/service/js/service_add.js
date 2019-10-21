$(function () {
    $('.width180').blur(function () {
        var idcard = $(this).val();
        $.getJSON('/service/checkCard/',
            {'idcard':idcard},
            function (data) {
                if(data['status']==200){
                    $('.validate_msg_short').html(data['msg']).css({'color': 'green', 'font-size': 10});
                }else{
                    $('.validate_msg_short').html(data['msg']).css({'color': 'red', 'font-size': 10});
                }
            }
        )
    })
    $('#checkAccount').blur(function () {
        var financial_account = $(this).val();
        $.getJSON('/service/checkCard/',
            {'financial_account':financial_account},
            function (data) {
                if(data['status']==200){
                    $('.validate_msg_long').html(data['msg']).css({'color': 'green', 'font-size': 10});
                }else{
                    $('.validate_msg_long').html(data['msg']).css({'color': 'red', 'font-size': 10});
                }
            }
        )
    })
})