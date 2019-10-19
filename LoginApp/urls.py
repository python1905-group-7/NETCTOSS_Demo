from django.conf.urls import url

from LoginApp import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^get_code/', views.get_code, name='get_code')
]