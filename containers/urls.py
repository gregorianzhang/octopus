from django.conf.urls import patterns, include, url
from containers import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='containers_list'),
    url(r'list/$', views.list, name='containers_list'),
    url(r'create/$', views.create, name='containers_create'),
    url(r'destroy/$', views.destroy, name='containers_destroy'),
    url(r'detail/(.+)$', views.detail, name='containers_detail'),
    url(r'start/$', views.start, name='containers_start'),
    url(r'stop/$', views.stop, name='containers_stop'),
    url(r'restart/$', views.restart, name='containers_restart'),
)
