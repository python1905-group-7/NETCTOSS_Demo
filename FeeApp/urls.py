from django.conf.urls import url

from FeeApp import views

urlpatterns = [
    url(r'^fee_list/', views.fee_list, name='fee_list'),
    url(r'^get_cost_list/', views.CostView.as_view(), name='get_cost_list'),
    url(r'^update_to_cost_status/', views.update_to_cost_status, name='update_to_cost_status'),
    url(r'^update_to_cost/', views.update_to_cost, name='update_to_cost'),
    url(r'^delete_to_cost/', views.delete_to_cost, name='delete_to_cost'),
]
