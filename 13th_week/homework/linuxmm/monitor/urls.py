from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^login$',   views.login,   name="login"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^logout$',  views.logout,  name="logout"),

    url(r'^monitor/$', views.index, name='index'),
    url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),

    url(r'^monitor/add$', views.add, name='monitor_add'),
    url(r'^monitor/insert$', views.insert, name='monitor_insert'),
    url(r'^monitor/delete/(?P<hid>\d+)$', views.delete, name='monitor_delete'),
    url(r'^monitor/edit/(?P<hid>\d+)$', views.edit, name='monitor_edit'),
    url(r'^monitor/update/(?P<hid>\d+)$', views.update, name='monitor_update'),

    #url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),
    #url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),

    url(r'^monitor/details/(?P<hid>\d+)$', views.details, name='details'),
    url(r'^monitor/manual', views.manual, name='manual'),
    url(r'^monitor/settings', views.settings, name='settings'),
]
