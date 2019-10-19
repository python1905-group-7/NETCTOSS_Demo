from django.conf.urls import url

from TestApp import views

urlpatterns = [
    url(r'login', views.login)
]