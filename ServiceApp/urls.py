from django.conf.urls import url

from ServiceApp import views

urlpatterns = [
    url(r'^service_list/',views.service_list,name='service_list'),
    url(r'^pause/',views.pause,name='pause'),
    url(r'^service_searchid/',views.service_searchid,name='service_searchid'),
    url(r'^checkCard/',views.checkCard,name='checkCard'),
    url(r'^checkAccount/',views.checkAccount,name='checkAccount'),
    url(r'^service_add/',views.service_add,name='service_add'),
    url(r'^service_detail',views.service_detail,name='service_detail'),
    url(r'^find_cardid/',views.find_cardid,name='find_cardid'),

]