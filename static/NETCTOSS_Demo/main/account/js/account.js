var flag = 1;
$(function () {
    $(".btn_search").click(function () {
        var idcard = $(".text_search").val()
        var real_name = $(".text_search2").val()
        var login_name = $(".text_search3").val()
        var status = $(".select_search option:selected").text()

        $.getJSON('/account/account_searchid/',
            {
                'idcard': idcard,
                'real_name': real_name,
                'login_name': login_name,
                'status': status,
            },
            function (data) {
                if (data['status'] === 200) {

                    window.location.href = "/account/account_list/"
                }
            }
        )
    })
    $('.real_name').click(function () {
        window.location.href = '/account/account_detail/'
    })
    $('.btn_delete').click(function () {
        var id = $(this).attr('id');
        var $object = $(this).parent().prev().prev().prev();
        var $object1 = $(this).parent()
        alert('确定要删除此账务账号吗？删除后将不能恢复，且会删除其下属的所有业务账号')
        $.getJSON('/account/account_delete/',
            {'id': id},
            function (data) {
                if (data['status'] === 200) {
                    $object.html('删除');
                    $object1.toggle()
                }
            }
        )
    });

    $('.btn_pause').click(function () {

        var $btn_pause = $(this)
        var id1 = $(this).attr('id1');
        var $object = $(this).parent().prev().prev().prev();
        var $object1 = $(this).parent();

        $.getJSON('/account/account_stop/',
            {'id1': id1, 'flag': flag},
            function (data) {
                if (data['status'] === 200) {
                    if (data['flag'] === '1') {
                        $object.html('开通');
                        $btn_pause.val('暂停');
                        flag = 2
                    } else {
                        alert('确定要暂停此账务账号嘛？')
                        $object.html('暂停');
                        $btn_pause.val('开通');
                        flag = 1
                        window.location.href='/account/account_list'

                    }
          }


            }
        )

    })


     $('.btn_start').click(function () {

        var $btn_pause = $(this)
        var id1 = $(this).attr('id1');
        var $object = $(this).parent().prev().prev().prev();
        var $object1 = $(this).parent();

        $.getJSON('/account/account_stop/',
            {'id1': id1, 'flag': flag},
            function (data) {
                if (data['status'] === 200) {
                    if (data['flag'] === '1') {
                        alert('确定要开通此账务账号吗？')
                        $object.html('开通');
                        $btn_pause.val('暂停');
                        flag = 2
                    } else {
                        $object.html('暂停');
                        $btn_pause.val('开通');
                        flag = 1
                        alert('确定要暂停此账务账号嘛？')
                    }
              }

            }
        )

    })


});