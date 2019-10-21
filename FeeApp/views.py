from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import View

from FeeApp.models import Cost
from FeeApp.serializers import CostSerializers


def fee_list(request):
    return render(request, 'NETCTOSS_Demo/main/fee/fee_list.html')


def fee_modi(request):
    return render(request, 'NETCTOSS_Demo/main/fee/fee_modi.html')


class AllCostView(View):
    def get(self, request):
        data = dict()
        cost_list = Cost.objects.all()

        if cost_list.exists():
            costSerializers = CostSerializers(cost_list, many=True)
            data['msg'] = '获取成功!'
            data['status'] = 200
            data['data'] = costSerializers.data
        else:
            data['msg'] = '没有资费信息!'
            data['status'] = 404

        return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


class CostView(View):
    def get(self, request):
        data = dict()
        cost_id = request.GET.get('cost_id')
        cost = Cost.objects.filter(id=cost_id)

        if cost.exists():
            cost = cost.first()
            costSerializers = CostSerializers(cost)
            data['msg'] = '获取成功!'
            data['status'] = 200
            data['data'] = costSerializers.data
        else:
            data['msg'] = '没有该资费的信息!'
            data['status'] = 404

        return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


def update_to_cost_status(request):
    cost_id = int(request.GET.get('cost_id'))
    cost = Cost.objects.filter(id=cost_id)
    data = {
        'msg': '修改成功!',
        'status': 200
    }

    if cost.exists():
        cost = cost.first()
        cost.status = True
        cost.startime = timezone.now()
        cost.save()
        data['data'] = CostSerializers(cost).data.get('startime')
    else:
        data['msg'] = '没有该资费的信息!'
        data['status'] = 404

    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


# {
#     'name': $('#name').val(),
#     'base_duration': $('#base_duration').val(),
#     'base_cost': $('#base_cost').val(),
#     'unit_cost': $('#unit_cost').val(),
#     'descr': $('#descr').val(),
#     'cost_type': $('input[name="radFeeType"]:checked').val()
# }
def update_to_cost(request):
    values = dict()
    data = {
        'msg': '修改成功!',
        'status': 200
    }

    try:
        values['id'] = int(request.GET.get('id'))
        values['name'] = request.GET.get('name')
        values['descr'] = request.GET.get('descr')
        values['cost_type'] = request.GET.get('cost_type')
        if values['cost_type'] == '1':
            values['base_cost'] = float(request.GET.get('base_cost'))
        elif values['cost_type'] == '2':
            values['base_duration'] = request.GET.get('base_duration')
            values['base_cost'] = float(request.GET.get('base_cost'))
            values['unit_cost'] = float(request.GET.get('unit_cost'))
        elif values['cost_type'] == '3':
            values['unit_cost'] = float(request.GET.get('unit_cost'))
    except ValueError:
        data['msg'] = '数据类型错误!'
        data['status'] = 500

        return JsonResponse(data=data)
    cost = Cost.objects.filter(id=values['id'])
    if cost.exists():
        cost = cost.first()
        cost.name = values.get('name')
        cost.cost_type = values.get('cost_type')
        cost.base_duration = values.get('base_duration')
        cost.base_cost = values.get('base_cost')
        cost.unit_cost = values.get('unit_cost')
        cost.descr = values.get('descr')

        cost.save()
    else:
        data['msg'] = '没有该资费的信息!'
        data['status'] = 404

    return JsonResponse(data=data)


def delete_to_cost(request):
    cost_id = int(request.GET.get('cost_id'))
    cost = Cost.objects.filter(id=cost_id)
    data = {
        'msg': '删除成功!',
        'status': 200
    }

    if cost.exists():
        cost = cost.first()
        cost.status = None
        cost.save()
    else:
        data['msg'] = '没有该资费的信息!'
        data['status'] = 404

    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
