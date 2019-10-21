let cost;
let className = '';
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
    let radio_id = get_radio_id(data)
    $(radio_id).attr('checked', 'checked');
    $('#base_duration').val(data['base_duration']);
    $('#base_cost').val(data['base_cost']);
    $('#unit_cost').val(data['unit_cost']);
    feeTypeChange(parseInt(data['cost_type']));
    $('#descr').val(data['descr'])
}

//保存结果的提示
function showResult() {
    let value = {
        'id': cost['id'],
        'name': $('#name').val(),
        'base_duration': $('#base_duration').val(),
        'base_cost': $('#base_cost').val(),
        'unit_cost': $('#unit_cost').val(),
        'descr': $('#descr').val(),
        'cost_type': $('input[name="radFeeType"]:checked').val()
    };

    if (value['name'] === '') {
        className = 'save_result_info6';
        showResultDiv(true, className);
        window.setTimeout("showResultDiv(false, 'save_result_info6');", 3000);
    } else if (!value['cost_type']) {
        className = 'save_result_info7';
        showResultDiv(true, className);
        window.setTimeout("showResultDiv(false, 'save_result_info7');", 3000);
    } else if (parseInt(value['base_duration']) > 600 || parseInt(value['base_duration']) === 0) {
        className = 'save_result_info2';
        showResultDiv(true, className);
        window.setTimeout("showResultDiv(false, 'save_result_info2');", 3000);
    } else if (parseFloat(value['base_cost']) > 99999.99) {
        className = 'save_result_info3';
        showResultDiv(true, className);
        window.setTimeout("showResultDiv(false, 'save_result_info3');", 3000);
    } else if (parseFloat(value['unit_cost']) > 99999.99) {
        className = 'save_result_info4';
        showResultDiv(true, className);
        window.setTimeout("showResultDiv(false, 'save_result_info4');", 3000);
    } else {
        if (value['cost_type'] === '1') {
            if (value['base_cost'] === '') {
                className = 'save_result_info9';
                showResultDiv(true, className);
                window.setTimeout("showResultDiv(false, 'save_result_info9');", 3000);
            }
        } else if (value['cost_type'] === '2') {
            if (value['base_duration'] === '') {
                className = 'save_result_info8';
                showResultDiv(true, className);
                window.setTimeout("showResultDiv(false, 'save_result_info8');", 3000);
            } else if (value['base_cost'] === '') {
                className = 'save_result_info9';
                showResultDiv(true, className);
                window.setTimeout("showResultDiv(false, 'save_result_info9');", 3000);
            } else if (value['unit_cost'] === '') {
                className = 'save_result_info10';
                showResultDiv(true, className);
                window.setTimeout("showResultDiv(false, 'save_result_info10');", 3000);
            }
        } else if (value['cost_type'] === '3') {
            if (value['unit_cost'] === '') {
                className = 'save_result_info10';
                showResultDiv(true, className);
                window.setTimeout("showResultDiv(false, 'save_result_info10');", 3000);
            }
        } else {
            $.get(
                '/fee/update_to_cost/',
                value,
                function (data) {
                    if (data['status'] === 200) {
                        className = 'save_result_info1';
                        showResultDiv(true, className);
                        window.setTimeout("showResultDiv(false, className);", 3000);
                    } else if (data['status'] === 501) {
                        className = 'save_result_info5';
                        showResultDiv(true, className);
                        window.setTimeout("showResultDiv(false, className);", 3000);
                    }
                }
            );
        }
    }
}

function showResultDiv(flag, id) {
    let divResult = document.getElementsByClassName(id)[0];
    if (flag)
        divResult.style.display = "block";
    else
        divResult.style.display = "none";
}
