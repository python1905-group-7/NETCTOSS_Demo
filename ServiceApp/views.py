from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from AccountApp.models import Account
from FeeApp.models import Cost
from ServiceApp.models import Service

def judge_status1(status, service_list):
    service = service_list.filter(status=status)
    return service


def judge_identity1(idcard, service_list):
    account = Account.objects.filter(idcard_no=idcard)
    service = service_list.filter(account=account)

    return service


def judge_unix_host1(unix_host, service_list):
    service = service_list.filter(unix_host=unix_host)
    return service


def service_list(request):
    service_list = Service.objects.all()
    # 当前页
    page = request.GET.get('page', 1)
    # 当前页显示条目
    per_page = request.GET.get('per_page', 5)
    # 实例Praginator对象
    pagin = Paginator(service_list, per_page)
    #
    pages = pagin.page(page)
    context = {
        's_page': pages,
        'pagin': pagin,
    }
    return render(request, 'NETCTOSS_Demo/main/service/service_list.html', context=context)


#暂停
def pause(request):
    sid = request.GET.get('sid')
    service = Service.objects.get(pk=sid)
    service.pause_date = timezone.now()
    service.status = 0
    service.save()

    data = {
        'msg': 'ok',
        'status': 200
    }
    return JsonResponse(data=data)

#开通
def start(request):
    sid = request.GET.get('sid')
    service = Service.objects.get(pk=sid)
    service.pause_date = None
    service.status = 1
    service.save()

    data = {
        'msg': 'ok',
        'status': 200
    }
    return JsonResponse(data=data)

#删除
def delete(request):
    sid = request.GET.get('sid')
    service = Service.objects.get(pk=sid)
    service.close_date = timezone.now()
    service.status = None
    service.save()

    data = {
        'msg': 'ok',
        'status': 200
    }
    return JsonResponse(data=data)

#修改
def modify(request):
    service_id = request.GET.get('sid')
    service = Service.objects.get(pk=service_id)
    cost_list = Cost.objects.all()

    context = {
        's_id': service.id,
        'unix_host': service.unix_host,
        'os_username': service.os_username,
        'cost_list': cost_list
    }

    return render(request, 'NETCTOSS_Demo/main/service/modify_info.html', context=context)


# 数据库异常报错信息
class SQLError(Exception):
    def __str__(self):
        return "哦豁！出错了！"


def save_modify(request):
    service_id = request.POST.get('sid')
    costname = request.POST.get('costname')
    print('sid', service_id)
    print(costname)
    data = {
        'msg': 'ok',
        'status': 200
    }
    service = Service.objects.get(pk=service_id)
    service.cost = Cost.objects.filter(name=costname)[0]
    service.save()

    return JsonResponse(data=data)



# 增加
def service_add(request):
    cost_list = Cost.objects.all()
    cost_name_list = []
    for cost in cost_list:
        cost_name_list.append(cost.name)
    context = {
        'cost_name_list': cost_name_list
    }
    return render(request, 'NETCTOSS_Demo/main/service/service_add.html', context=context)


#查询身份证
def query_idcard_no(request):
    idcard_no = request.GET.get('idcard_No')
    account = Account.objects.filter(idcard_no=idcard_no)
    data = {
        'msg': 'ok',
        'status': 200
    }
    if account.count() > 0:
        data['msg'] = '该身份证存在.'
    else:
        data['msg'] = '没有此身份证号，请重新录入。'
        data['status'] = 201
    return JsonResponse(data=data)


#查询账务账号
def account_id_query(request):
    account_id = request.GET.get('account_id')
    data = {
        'msg': 'ok',
        'status': 200
    }
    account = Account.objects.filter(pk=account_id)

    if account.count() > 0:
        data['msg'] = '该账号存在.'
    else:
        data['msg'] = '没有此账号，请重新录入。'
        data['status'] = 201
    return JsonResponse(data=data)

#添加到service
def add_service(request):
    # idcard = request.POST.get('idcard')
    accountid = request.POST.get('accountid')
    costname = request.POST.get('costname')
    unix_host = request.POST.get('unix_host')
    os_account = request.POST.get('os_account')
    password = request.POST.get('password')

    data = {
        'msg': 'ok',
        'status': 200
    }

    cost = Cost.objects.filter(name=costname)[0]

    account = Account.objects.filter(id=accountid)

    if account.count() > 0:

        services = Service.objects.filter(account=account)

        if services.filter(status=True).count()>0 :
            service = Service()
            service.account_id = accountid
            service.unix_host = unix_host

            service.login_passwd = make_password(password)
            service.os_username = os_account
            service.cost = cost
            services.status = True
            service.save()
        else:
            data['msg'] = '该账务账号下有暂停或删除状态的账号'
            data['status'] = 202
    else:
        data['msg'] = '账务账号不存在'
        data['status'] = 201

    return JsonResponse(data=data)
