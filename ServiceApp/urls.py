from django.conf.urls import url

from ServiceApp import views

urlpatterns = [
    url(r'^test/',views.test,name='test'),
    url(r'^pause/',views.pause,name='pause'),
]