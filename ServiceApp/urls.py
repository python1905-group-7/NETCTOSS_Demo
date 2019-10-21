from django.conf.urls import url

from ServiceApp import views

urlpatterns = [
    url(r'^service_list/',views.service_list,name='service_list'),
    url(r'^pause/',views.pause,name='pause'),
    url(r'^start/',views.start,name='start'),
    url(r'^delete/',views.delete,name='delete'),
    url(r'^modify/',views.modify,name='modify'),
    url(r'^save_modify/',views.save_modify,name='save_modify'),

    url(r'^service_add/',views.service_add,name='service_add'),
    url(r'^query_idcard_no/',views.query_idcard_no,name='query_idcard_no'),
    url(r'^account_id_query/',views.account_id_query,name='account_id_query'),
    url(r'^add_service/',views.add_service,name='add_service')
    url(r'^service_searchid/',views.service_searchid,name='service_searchid'),
    url(r'^checkCard/',views.checkCard,name='checkCard'),
    url(r'^checkAccount/',views.checkAccount,name='checkAccount'),
    url(r'^service_add/',views.service_add,name='service_add'),
    url(r'^service_detail',views.service_detail,name='service_detail'),
    url(r'^find_cardid/',views.find_cardid,name='find_cardid'),


]