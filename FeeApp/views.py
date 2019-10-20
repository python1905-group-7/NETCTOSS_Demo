from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
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
