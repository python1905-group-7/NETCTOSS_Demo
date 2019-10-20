from datetime import time

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from ServiceApp.models import Service


def test(request):
    service_list=Service.objects.all()
    #当前页
    page = request.GET.get('page',1)
    #当前页显示条目
    per_page=request.GET.get('per_page',5)
    #实例Praginator对象
    pagin = Paginator(service_list,per_page)
    #
    pages=pagin.page(page)
    context={
        's_page':pages,
        'pagin':pagin,
    }
    return render(request,'NETCTOSS_Demo/main/service/service_list.html',context=context)


def pause(request):
    sid = request.GET.get('sid')
    service = Service.objects.get(pk=sid)
    service.pause_date=timezone.now()
    print(4444)
    data ={
        'msg':'ok',
        'status':200
    }
    return JsonResponse(data=data)