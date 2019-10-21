let cost;
$(function () {
    init()
});

function init() {
    let str = window.location.href;
    let value_str = str.substr(str.indexOf('?') + 1);
    let cost_id;
    let value_list = value_str.split('&');

    for (let i = 0; i < value_list.length; i++) {
        let value = value_list[i].split('=');
        if (value[0] === 'cost_id') {
            cost_id = value[1]
        }
    }


    $.get(
        '/fee/get_cost',
        {'cost_id': cost_id},
        function (data) {
            if (data['status'] === 200) {
                console.log(data);
                cost = data['data']
                set_form(cost);
            } else {
                window.location.href = '/fee/fee_list/'
            }
        }
    )
}

function set_form(data) {
    $('#id').val(data['id']);
    $('#name').val(data['name']);
    let radio_id = ['#monthly', '#package', '#timeBased'][parseInt(data['cost_type']) - 1];
    $(radio_id).attr('checked', 'checked');
    $('#base_duration').val(data['base_duration']);
    $('#base_cost').val(data['base_cost']);
    $('#unit_cost').val(data['unit_cost']);
    feeTypeChange(parseInt(data['cost_type']));
    $('#descr').val(data['descr'])
}

//保存结果的提示
function showResult() {
    $.get(
        '/fee/update_to_cost/',
        {
            'id': cost['id'],
            'name': $('#name').val(),
            'base_duration': $('#base_duration').val(),
            'base_cost': $('#base_cost').val(),
            'unit_cost': $('#unit_cost').val(),
            'descr': $('#descr').val(),
            'cost_type': $('input[name="radFeeType"]:checked').val()
        },
        function (data) {
            console.log(data)
            if (data['status'] === 200) {
                showResultDiv(true);
                window.setTimeout("showResultDiv(false);", 3000);
            }
        }
    );
}

function showResultDiv(flag) {
    let divResult = document.getElementById("save_result_info");
    if (flag)
        divResult.style.display = "block";
    else
        divResult.style.display = "none";
}

//切换资费类型
function feeTypeChange(type) {
    let base_duration = $('#base_duration');
    let base_cost = $('#base_cost');
    let unit_cost = $('#unit_cost');

    if (type === 1) {
        base_duration.val('');
        unit_cost.val('');

        base_duration.nextAll('.required').html('');
        base_cost.nextAll('.required').html('*');
        unit_cost.nextAll('.required').html('');

        base_duration.attr('readonly', 'readonly');
        base_cost.removeAttr('readonly');
        unit_cost.attr('readonly', 'readonly');

        base_duration.addClass('readonly');
        base_cost.removeClass('readonly');
        unit_cost.addClass('readonly');
    } else if (type === 2) {

        base_duration.nextAll('.required').html('*');
        base_cost.nextAll('.required').html('*');
        unit_cost.nextAll('.required').html('*');

        base_duration.removeAttr('readonly');
        base_cost.removeAttr('readonly');
        unit_cost.removeAttr('readonly');

        base_duration.removeClass('readonly');
        base_cost.removeClass('readonly');
        unit_cost.removeClass('readonly');
    } else if (type === 3) {
        base_duration.nextAll('.required').html('');
        base_cost.nextAll('.required').html('');
        unit_cost.nextAll('.required').html('*');

        base_duration.val('');
        base_cost.val('');

        base_duration.attr('readonly', 'readonly');
        base_cost.attr('readonly', 'readonly');
        unit_cost.removeAttr('readonly');

        base_duration.addClass('readonly');
        base_cost.addClass('readonly');
        unit_cost.removeClass('readonly');
    }
}