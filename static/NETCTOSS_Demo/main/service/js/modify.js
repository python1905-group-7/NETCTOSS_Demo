$(function () {
    $('#save').click(function () {
        var sid = $('input[name="sid"]').val();
        var select = $('select option:selected').val();
        $.ajax({
            url:'/service/save_modify/',
            data:{'sid':sid,'costname':select},
            type:'POST',
            dataType:'json',
            success:function (data) {
                if (data['status']==200){
                    location.href='/service/service_list/';
                }else {
                    $(".save_fail").show();
                    var m = window.setTimeout(function (){$(".save_fail").hide()},3000);
                    }
                }
            }

        );

    });
});