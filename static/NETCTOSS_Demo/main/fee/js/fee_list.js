let page_num = 1;
let page_size = 5;
let page_max;
let cost_list = [];

$(function () {
    init()
});

function init() {
    $.get(
        '/fee/get_cost_list',
        {},
        function (data) {
            cost_list = data['data'];
            page_max = Math.ceil(cost_list.length / page_size);
            set_datalist(cost_list);
            set_pages(1)
        }
    )
}

function set_datalist(data) {
    let trs = '<tr>\n' +
        '<th>资费ID</th>\n' +
        '<th class="width100">资费名称</th>\n' +
        '<th>基本时长</th>\n' +
        '<th>基本费用</th>\n' +
        '<th>单位费用</th>\n' +
        '<th>创建时间</th>\n' +
        '<th>开通时间</th>\n' +
        '<th class="width50">状态</th>\n' +
        '<th class="width200"></th>\n' +
        '</tr>';

    for (let i = (page_num - 1) * page_size; i < page_num * page_size; i++) {
        if (data[i]) {
            let btns = '<input type="button" value="启用" class="btn_start" onclick="startFee(' + i + ', ' + data[i]['id'] + ');"/>\n' +
                '<input type="button" value="修改" class="btn_modify" onclick="location.href=\'fee_modi.html\';"/>\n' +
                '<input type="button" value="删除" class="btn_delete" onclick="deleteFee(' + i + ', ' + data[i]['id'] + ');"/>\n';
            trs += '<tr>\n' +
                '<td>' + data[i]['id'] + '</td>\n' +
                '<td><a href="fee_detail.html">' + data[i]['name'] + '</a></td>\n' +
                '<td>' + (data[i]['base_duration'] ? data[i]['base_duration'] + ' 小时' : '') + '</td>\n' +
                '<td>' + (data[i]['base_cost'] ? data[i]['base_cost'] + ' 元' : '') + '</td>\n' +
                '<td>' + (data[i]['unit_cost'] ? data[i]['unit_cost'] + ' 元/小时' : '') + '</td>\n' +
                '<td>' + data[i]['creatime'] + '</td>\n' +
                '<td>' + (data[i]['startime'] ? data[i]['startime'] : '') + '</td>\n' +
                '<td>' + (data[i]['status'] ? '开通' : data[i]['status'] == null ? '删除' : '暂停') + '</td>\n' +
                '<td>\n' +
                (data[i]['status'] ? '' : data[i]['status'] == null ? '' : btns) +
                '</td>\n' +
                '</tr>'
        }
    }

    $('#datalist').html(trs);
}

function set_pages(page_num_) {
    if (page_max === 0) {
        return null;
    }

    page_num = page_num_;

    let pages = '<a onclick="set_pages(1)">首页</a>\n';

    if (page_num === 1) {
        pages += '<a onclick="set_pages(1)">上一页</a>\n';
    } else {
        pages += '<a onclick="set_pages(page_num - 1)">上一页</a>\n';
    }

    if (page_max <= 5) {
        for (let i = 1; i <= page_max; i++) {
            if (i === page_num) {
                pages += '<a onclick="set_pages(' + i + ')" class="current_page">' + i + '</a>\n'
            } else {
                pages += '<a onclick="set_pages(' + i + ')">' + i + '</a>\n'
            }
        }
    } else {
        if (page_num < 4) {
            for (let i = 1; i <= 5; i++) {
                if (i === page_num) {
                    pages += '<a onclick="set_pages(' + i + ')" class="current_page">' + i + '</a>\n'
                } else {
                    pages += '<a onclick="set_pages(' + i + ')">' + i + '</a>\n'
                }
            }
        } else if (page_num > page_max - 3) {
            for (let i = page_max - 4; i <= page_max; i++) {
                if (i === page_num) {
                    pages += '<a onclick="set_pages(' + i + ')" class="current_page">' + i + '</a>\n'
                } else {
                    pages += '<a onclick="set_pages(' + i + ')">' + i + '</a>\n'
                }
            }
        } else {
            for (let i = page_num - 2; i <= page_num + 2; i++) {
                if (i === page_num) {
                    pages += '<a onclick="set_pages(' + i + ')" class="current_page">' + i + '</a>\n'
                } else {
                    pages += '<a onclick="set_pages(' + i + ')">' + i + '</a>\n'
                }
            }
        }
    }

    if (page_num === page_max) {
        pages += '<a onclick="set_pages(page_max)">下一页</a>\n';
    } else {
        pages += '<a onclick="set_pages(page_num + 1)">下一页</a>\n';
    }

    pages += '<a onclick="set_pages(page_max)">末页</a>\n';

    $('#pages').html(pages);
    set_datalist(cost_list);
}

//排序按钮的点击事件
function sort(btnObj, code) {
    code = ['unit_cost', 'base_cost', 'base_duration'][code];

    let len = cost_list.length;

    if (btnObj.className === "sort_desc") {
        btnObj.className = "sort_asc";
        for (let i = 0; i < len - 1; i++) {
            for (let j = 0; j < len - 1 - i; j++) {
                if (parseFloat(cost_list[j][code]) > parseFloat(cost_list[j + 1][code])) {
                    let temp = cost_list[j];
                    cost_list[j] = cost_list[j + 1];
                    cost_list[j + 1] = temp;
                }
            }
        }
    } else {
        btnObj.className = "sort_desc";

        for (let i = 0; i < len - 1; i++) {
            for (let j = 0; j < len - 1 - i; j++) {
                if (parseFloat(cost_list[j][code]) < parseFloat(cost_list[j + 1][code])) {
                    let temp = cost_list[j];
                    cost_list[j] = cost_list[j + 1];
                    cost_list[j + 1] = temp;
                }
            }
        }
    }

    set_datalist(cost_list);
}

//启用
function startFee(sub_num, cost_id) {
    let r = window.confirm("确定要启用此资费吗？资费启用后将不能修改和删除。");
    if (r) {
        $.get(
            '/fee/update_to_cost_status/',
            {'cost_id': cost_id},
            function (data) {
                if (data['status'] === 200) {
                    cost_list[sub_num]['status'] = true;
                    cost_list[sub_num]['startime'] = data['data'];
                    set_datalist(cost_list);
                    document.getElementsByClassName("save_success")[0].style.display = "block";
                } else {
                    document.getElementsByClassName("save_error")[0].style.display = "block";
                }
            }
        )

    }
}

//删除
function deleteFee(sub_num, cost_id) {
    let r = window.confirm("确定要删除此资费吗？");
    if (r) {
        $.get(
            '/fee/delete_to_cost/',
            {'cost_id': cost_id},
            function (data) {
                if (data['status'] === 200) {
                    cost_list[sub_num]['status'] = null;
                    set_datalist(cost_list);
                    document.getElementsByClassName("operate_success")[0].style.display = "block";
                } else {
                    document.getElementsByClassName("operate_error")[0].style.display = "block";
                }
            }
        )
    }
}