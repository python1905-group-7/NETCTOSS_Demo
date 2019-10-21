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
                        $btn.val('开通');
                        $btn.toggleClass('btn_pause btn_start');
                    }
                }
            );
        }
    });

    $('.btn_start').click(function () {
        var sid = $(this).parent().attr('sid');
        var $btn = $(this);
        var $status = $(this).parent().prev().prev().prev();
        alert('开通按钮')
        if ($status.html() == '开通'){
            return;
        }else {
            $.get(
                '/service/start/',
                {'sid':sid},
                function (data) {
                    alert('ss')
                    if(data['status'] == 200){
                        $status.html('开通');
                        $btn.val('暂停');
                        $btn.toggleClass('btn_pause btn_start');
                        alert($btn.attr('class'));
                    }
                }
            );
        }
    });

    $('.btn_delete').click(function () {
        var r = window.confirm("确定要删除此业务账号吗？删除后将不能恢复。");
        if (r){
            var sid = $(this).parent().attr('sid');
            var $btn = $(this);
            var $status = $(this).parent().prev().prev().prev();
             $.get(
                '/service/delete/',
                {'sid':sid},
                function (data) {
                    if(data['status'] == 200){
                        $status.html('删除');
                       $btn.parent().html('');
                       document.getElementById("operate_result_info").style.display = "block";
                    }
                }
            );
        }else {
            return;
        }


    });

        $('.btn_modify').click(function () {
        var sid = $(this).parent().attr('sid');
        var $btn = $(this);
        var $status = $(this).parent().prev().prev().prev();

        $.get(
            '/service/modify/',
            {'sid':sid},
            function (data) {
                if(data['status'] == 200){
                    location.href('/service/');
                }
            }
        );

    });
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