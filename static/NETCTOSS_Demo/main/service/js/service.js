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
    $(".btn_search").click(function () {
        var os_username = $(".text_search1").val()
        var unix_host = $(".text_search2").val()
        var idcard = $(".text_search3").val()
        var status = $(".select_search option:selected").text()

        $.getJSON('/service/service_searchid/',
            {
                'idcard': idcard,
                'os_username': os_username,
                'unix_host': unix_host,
                'status': status,
            },
            function (data) {
                if (data['status'] === 200) {

                    window.location.href = "/service/test/"
                }
            }
        )
    })

})