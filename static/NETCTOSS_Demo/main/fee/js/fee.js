$(function () {
    $.get(
        '/login/get_user/',
        {},
        function (data) {
            if (data['status'] === 200) {
                $('#header').find('b').html(data['data']['admin_code']);
            } else {
                console.log(123)
                window.location.href = '/login/'
            }
        }
    )
});

function get_cost_id() {
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

    return cost_id
}

function get_radio_id(data) {
    return ['#monthly', '#package', '#timeBased'][parseInt(data['cost_type']) - 1];
}

function set_base_duration(input) {
    let value = $(input).val();
    value = value.replace(/[^\d]/g, '');
    $(input).val(value);
}

function set_price(input) {
    let value = $(input).val()
    value = value.replace(/[^\d\.]/g, '');
    value = value.replace(/^\./g, '');
    value = value.replace(/\.{2,}/g, '.');
    value = value.replace('.', '$#$').replace(/\./g, '').replace('$#$', '.');
    if ((parseFloat(value) * 100) % 100) {
        value = Math.floor(parseFloat(value) * 100) / 100
    }
    $(input).val(value)
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