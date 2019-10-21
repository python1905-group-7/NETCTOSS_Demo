import datetime

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


from AccountApp.models import Account


def judge_status(status, accounts):
    account = accounts.filter(status=status)
    return account


def judge_identity(idcard, accounts):
    account = accounts.filter(idcard_no=idcard)
    print(account)
    return account


def judge_name(real_name, accounts):
    account = accounts.filter(real_name=real_name)
    return account


def judge_login_name(login_name, accounts):
    account = accounts.filter(login_name=login_name)
    return account


def account_list(request):
    idcard = request.session.get('idcard')
    real_name = request.session.get('real_name')
    login_name = request.session.get('login_name')
    status = request.session.get('status')

    if status == '删除':
        status = '0'
    elif status == '开通':
        status = '1'
    elif status == '暂停':
        status = '2'
    else:
        status = None

    accounts = Account.objects.all()
    if status:
        accounts = judge_status(status, accounts)
    if idcard:
        accounts = judge_identity(idcard, accounts)
    if real_name:
        accounts = judge_name(real_name, accounts)
    if login_name:
        accounts = judge_login_name(login_name, accounts)


    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 3)
    pagin = Paginator(accounts, per_page)
    p = pagin.page(page)

    context = {
        'p': p,
        'pagin': pagin,
        'page': int(page),
    }
    request.session.flush()
    return render(request, 'NETCTOSS_Demo/main/account/account_list.html', context=context)


def account_add(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_add.html')


def account_detail(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_detail.html')


def account_modi(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_modi.html')


def account_searchid(request):
    idcard = request.GET.get('idcard')
    real_name = request.GET.get('real_name')
    login_name = request.GET.get('login_name')
    status = request.GET.get('status')
    request.session['idcard'] = idcard
    request.session['real_name'] = real_name
    request.session['login_name'] = login_name
    request.session['status'] = status
    data = {
        'msg': 'ok',
        'status': 200
    }

    return JsonResponse(data=data)


def account_delete(request):
    id = request.GET.get('id')
    account = Account.objects.get(pk=id)
    account.status = '0'
    account.close_date=datetime.datetime.now()
    account.save()
    data = {
        'msg': 'ok',
        'status': 200,
        'account': account.get()
    }
    return JsonResponse(data=data)


def account_stop(request):

    id1 = request.GET.get('id1')
    flag = request.GET.get('flag')
    if flag == '1':
        account = Account.objects.get(pk=id1)
        account.status = '1'
        account.last_login_time=None
        account.pause_date =None


        account.save()

    else:

        account = Account.objects.get(pk=id1)
        account.status = '2'
        # account.pause_date =None
        account.last_login_time=datetime.datetime.now()
        Account.last_login_time=None

        account.save()

    data = {
        'msg': 'ok',
        'status': 200,
        'account': account.get(),
        'flag': flag,

    }

    return JsonResponse(data=data)
