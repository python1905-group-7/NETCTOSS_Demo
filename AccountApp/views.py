from django.shortcuts import render


def account_list(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_list.html')


def account_add(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_add.html')


def account_modi(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_modi.html')


def account_detail(request):
    return render(request, 'NETCTOSS_Demo/main/account/account_detail.html')



