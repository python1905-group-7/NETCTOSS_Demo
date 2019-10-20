$(function () {
    $('.btn_pause').click(function () {
        var sid = $(this).parent().attr('sid');
        var $btn = $(this);
        var $status = $(this).parent().prev().prev().prev();
        if ($status.html() == '暂停'){
            return;
        }else {
            $.get(
                '/service/pause/',
                {'sid':sid},
                function (data) {
                    if(data['status'] == 200){
                        $status.html('暂停');
                        $btn.val('开始');
                        $btn.toggleClass('btn_pause btn_start');
                    }
                }
            );
        }



    })


})