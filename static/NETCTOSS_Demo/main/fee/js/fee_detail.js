let cost;
$(function () {
    init()
});

function init() {
    let cost_id = get_cost_id();

    $.get(
        '/fee/get_cost',
        {'cost_id': cost_id},
        function (data) {
            if (data['status'] === 200) {
                cost = data['data'];
                set_main(cost);
            } else {
                window.location.href = '/fee/fee_list/';
            }
        }
    )
}

function set_main(data) {
    $('#id').val(data['id']);
    $('#name').val(data['name']);
    if (data['status']){
        $('#status').html('开通')
    } else {
        if (data['status'] === false) {
            $('#status').html('暂停')
        } else {
            $('#status').html('删除')
        }
    }
    let radio_id = get_radio_id(data);
    $(radio_id).attr('checked', 'checked');
    $('#base_duration').val(data['base_duration']);
    $('#base_cost').val(data['base_cost']);
    $('#unit_cost').val(data['unit_cost']);
    $('#creatime').val(data['creatime']);
    $('#startime').val(data['startime']);
    $('#descr').val(data['descr'])
}