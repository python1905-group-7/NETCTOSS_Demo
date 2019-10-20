from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import View

from FeeApp.models import Cost
from FeeApp.serializers import CostSerializers


def fee_list(request):
    return render(request, 'NETCTOSS_Demo/main/fee/fee_list.html')


class CostView(View):
    def get(self, request):

        cost_list = Cost.objects.all()
        costSerializers = CostSerializers(cost_list, many=True)

        data = {
            'msg': '获取成功!',
            'status': 200,
            'data': costSerializers.data
        }

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


def update_to_cost(request):
    return None


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
