from django.conf.urls import url

from AccountApp import views

urlpatterns = [
    url(r'^check_name/', views.check_name, name='check_name'),
    url(r'^check_identity/', views.check_identity, name='check_identity'),
    url(r'^check_account/', views.check_account, name='check_account'),
    url(r'^check_old_pwd/', views.check_old_pwd, name='check_old_pwd'),
    url(r'^check_pwd/', views.check_pwd, name='check_pwd'),
    url(r'^confirm_pwd/', views.confirm_pwd, name='confirm_pwd'),
    url(r'^check_tel/', views.check_tel, name='check_tel'),
    url(r'^check_email/', views.check_email, name='check_email'),
    url(r'^check_mailaddress/', views.check_mailaddress, name='check_mailaddress'),
    url(r'^check_zipcode/', views.check_zipcode, name='check_zipcode'),
    url(r'^check_qq/', views.check_qq, name='check_qq'),

    url(r'^account_list/', views.account_list, name='account_list'),
    url(r'^account_searchid/', views.account_searchid, name='account_searchid'),
    url(r'^account_delete/', views.account_delete, name='account_delete'),
    url(r'^account_stop/', views.account_stop, name='account_stop'),

    url(r'^account_add/', views.account_add, name='account_add'),
    url(r'^add_user/', views.add_user, name='add_user'),

    url(r'^account_modi/', views.account_modi, name='account_modi'),
    url(r'^save_modifications/', views.save_modifications, name='save_modifications'),

    url(r'^account_detail/', views.account_detail, name='account_detail'),
    url(r'^find_name/', views.find_name, name='find_name')
]
