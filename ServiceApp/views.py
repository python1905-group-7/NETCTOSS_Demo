from datetime import time

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


def judge_os_username1(os_username,service_list):
    service = service_list.filter(os_username=os_username)
    return service


def service_list(request):
    idcard = request.session.get('idcard')

    status = request.session.get('status')
    os_username = request.session.get('os_username')
    unix_host = request.session.get('unix_host')
    print(status)
    if status == '删除':
        status = None
    elif status == '开通':
        status = '1'
    elif status == '暂停':
        status = '0'
    else:
        status = False

    service_list = Service.objects.all()


    if status != False:
        service_list = judge_status1(status, service_list)
    if idcard:
        service_list = judge_identity1(idcard, service_list)
    if unix_host:
        service_list = judge_unix_host1(unix_host, service_list)
    if os_username:
        service_list = judge_os_username1(os_username, service_list)


    #当前页
    page = request.GET.get('page',1)
    #当前页显示条目
    per_page=request.GET.get('per_page',5)
    #实例Praginator对象
    pagin = Paginator(service_list,per_page)
    #
    pages=pagin.page(page)
    p = pagin.page(page)
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



def service_searchid(request):

    os_username = request.GET.get('os_username')
    unix_host = request.GET.get('unix_host')
    idcard = request.GET.get('idcard')
    status = request.GET.get('status')
    request.session['os_username'] = os_username
    request.session['unix_host'] = unix_host
    request.session['idcard'] = idcard
    request.session['status'] = status
    data = {
        'msg': 'ok',
        'status': 200
    }

    return JsonResponse(data=data)

    #检查身份证是否存在
def checkCard(request):
    idcard = request.GET.get('idcard')
    idcards = Account.objects.filter(idcard_no=idcard)



    data = {
        'msg': '核对正确',
        'status': 200,
    }
    if not idcards:
        data['msg'] = '没有此身份证号，请重新录入。',
        data['status'] = 201


    return JsonResponse(data=data)

    #检查财务账号是否存在
def checkAccount(request):
    financial_account = request.GET.get('financial_account')

    financial_accounts = Account.objects.filter(id=financial_account)


    data= {
        'msg':'核对正确',
        'status':200
    }

    if not financial_accounts:
        data['smg']='没有此账务账号，请重新录入。'
        data['status'] = 201
    return JsonResponse(data=data)


def service_add(request):
    if request.method == 'GET':
        return render(request,'NETCTOSS_Demo/main/service/service_add.html')
    if request.method == 'POST':
        idcard = request.POST.get('idcard')
        # 财务账号
        financial_account = request.POST.get('financial_account')
        unix_host = request.POST.get('unix_host')
        os_username = request.POST.get('os_username')
        login_passwd = request.POST.get('login_passwd')


        service = Service()
        service.account.idcard_no = idcard
        service.account_id = financial_account
        service.unix_host = unix_host
        service.os_username = os_username
        service.login_passwd = login_passwd
        service.save()


    return render(request,'NETCTOSS_Demo/main/service/service_list.html')


def service_detail(request):
    sid = request.GET.get('sid')
    print(sid)
    service = Service.objects.get(pk=sid)
    context={
        'service':service
    }

    return render(request,'NETCTOSS_Demo/main/service/service_detail.html',context=context)


def find_cardid(request):
    idcard = request.GET.get('idcard')
    request.session['cardid'] = idcard
    return JsonResponse({})