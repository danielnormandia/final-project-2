from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.fact_show, name='fact_show'),
    url(r'^fact/new/$', views.fact_new, name='fact_new'),
    url(r'^fact/(?P<pk>\d+)/$', views.fact_detail, name='fact_detail'),
    url(r'^fact/(?P<pk>\d+)/remove/$', views.fact_remove, name='fact_remove'),
]
