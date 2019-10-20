from django.conf.urls import url

from AccountApp import views

urlpatterns = [
    url(r'^account_list/', views.account_list, name='account_list'),

    url(r'^account_add/', views.account_add, name='account_add'),
    url(r'^check_name/', views.check_name, name='check_name'),
    url(r'^check_identity/', views.check_identity, name='check_identity'),
    url(r'^check_account/', views.check_account, name='check_account'),
    url(r'^check_pwd/', views.check_pwd, name='check_pwd'),
    url(r'^confirm_pwd/', views.confirm_pwd, name='confirm_pwd'),
    url(r'^check_tel/', views.check_tel, name='check_tel'),
    url(r'^add_user/', views.add_user, name='add_user'),

    url(r'^account_modi/', views.account_modi, name='account_modi'),

    url(r'^account_detail/', views.account_detail, name='account_detail'),

    url(r'^find_name/', views.find_name, name='find_name')
]
