import re

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from AccountApp.models import Account, Recommender


def account_list(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_list.html')


def account_add(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_add.html')


def judge(res):
    if res:
        return True
    return False


def check_name(request):
    name = request.GET.get('name')
    res = re.match(r'[\u4e00-\u9fa5a-zA-Z0-9]{1,20}$', name)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_identity(request):
    identity = request.GET.get('identity')
    res = re.match(r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',
                   identity)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_account(request):
    account = request.GET.get('account')
    res = re.match(r'[a-zA-Z0-9_]{1,30}$', account)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_old_pwd(request):
    o_pwd = request.GET.get('o_pwd')
    a_id = int(request.GET.get('a_id'))
    pwd = Account.objects.get(pk=a_id)
    flag = o_pwd == pwd
    return JsonResponse({'flag': flag})


def check_pwd(request):
    pwd = request.GET.get('pwd')
    res = re.match(r'[a-zA-Z0-9_]{6,16}$', pwd)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def confirm_pwd(request):
    pwd = request.GET.get('pwd')
    c_pwd = request.GET.get('c_pwd')
    flag = pwd == c_pwd
    return JsonResponse({'flag': flag})


def check_tel(request):
    tel = request.GET.get('tel')
    res = re.match(r'\d{11}$', tel)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_email(request):
    email = request.GET.get('email')
    res = re.match(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_mailaddress(request):
    mailaddress = request.GET.get('mailaddress')
    res = re.match(r'\d{1,50}$', mailaddress)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_zipcode(request):
    zipcode = request.GET.get('zipcode')
    res = re.match(r'\d{6}$', zipcode)
    flag = judge(res)
    return JsonResponse({'flag': flag})


def check_qq(request):
    qq = request.GET.get('qq')
    res = re.match(r'\d{5,13}$', qq)
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
            r_id = Recommender.objects.get(pk=account.recommender_id).id
            r_idcard_no = Recommender.objects.get(pk=account.recommender_id).idcard_no
        else:
            r_id = ''
            r_idcard_no = ''
        data['account'] = account
        data['r_id'] = r_id
        data['r_idcard_no'] = r_idcard_no
    return render(request, 'NETCTOSS_Demo/main/account/account_detail.html', context=data)


def find_name(request):
    real_name = request.GET.get('real_name')
    request.session['real_name'] = real_name
    return JsonResponse({})
