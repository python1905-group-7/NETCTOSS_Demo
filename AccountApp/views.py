import re

from django.contrib.auth.hashers import make_password
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
from django.shortcuts import render, redirect
from django.urls import reverse

from AccountApp.models import Account, Recommender

def judge_login_name(login_name, accounts):
    account = accounts.filter(login_name=login_name)
    return account


def account_list(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_list.html')
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


def judge(res):
    if res:
        return True
    return False


def check_name(request):
    name = request.GET.get('name')
    res = re.match(r'[\u4e00-\u9fa5a-zA-Z0-9]{1,20}', name)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_identity(request):
    identity = request.GET.get('identity')
    res = re.match(r'', identity)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_account(request):
    account = request.GET.get('account')
    res = re.match(r'[a-zA-Z0-9_]{1,30}', account)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_pwd(request):
    pwd = request.GET.get('pwd')
    res = re.match(r'[a-zA-Z0-9_]{6,16}', pwd)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def confirm_pwd(request):
    pwd = request.GET.get('pwd')
    c_pwd = request.GET.get('c_pwd')
    flag = pwd == c_pwd
    return JsonResponse({'flag': flag})


def check_tel(request):
    tel = request.GET.get('tel')
    res = re.match(r'\d{11}', tel)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def add_user(request):
    name = request.GET.get('name')
    identity = request.GET.get('identity')
    account = request.GET.get('account')
    pwd = request.GET.get('pwd')
    pwd = make_password(pwd)
    tel = request.GET.get('tel')
    user = Account()
    user.real_name = name
    user.idcard_no = identity
    user.login_name = account
    user.login_passwd = pwd
    user.telephone = tel
    user.save()
    return redirect(reverse('account:account_add'))


def account_modi(request):
    data = {}
    real_name = request.session.get('real_name')
    if real_name:
        account = Account.objects.filter(real_name=real_name)[0]
        data['account'] = account
    return render(request, 'NETCTOSS_Demo/main/account/account_modi.html', context=data)


def account_detail(request):
    data = {}
    real_name = request.session.get('real_name')
    if real_name:
        account = Account.objects.filter(real_name=real_name)[0]
        if account.recommender_id:
            r_id = Recommender.objects.get(account.recommender_id).id
            r_idcard_no = Recommender.objects.get(account.recommender_id).idcard_no
        else:
            r_id = ''
            r_idcard_no = ''
        data['account'] = account
        data['r_id'] = r_id
        data['r_idcard_no'] = r_idcard_no
    return render(request, 'NETCTOSS_Demo/main/account/account_detail.html', context=data)

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

def find_name(request):
    real_name = request.GET.get('real_name')
    request.session['real_name'] = real_name
    return JsonResponse({})
