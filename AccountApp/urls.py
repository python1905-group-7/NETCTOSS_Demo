from django.conf.urls import url

from AccountApp import views

urlpatterns = [
    url(r'^account_list/', views.account_list, name='account_list'),
    url(r'^account_add/', views.account_add, name='account_add'),
    url(r'^account_modi/', views.account_modi, name='account_modi'),
    url(r'^account_detail/', views.account_detail, name='account_detail'),
]
