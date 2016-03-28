from django.conf.urls import include, url

from account import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
