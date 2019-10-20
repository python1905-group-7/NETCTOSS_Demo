from django.conf.urls import url

from FeeApp import views

urlpatterns = [
    url(r'^fee_list/', views.fee_list, name='fee_list'),
    url(r'^get_cost_list/', views.CostView.as_view(), name='get_cost_list'),
]