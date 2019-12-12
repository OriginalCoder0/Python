from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_host_stat/(?P<ip4addr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$', views.get_host_stat, name='getHostStat'),
]