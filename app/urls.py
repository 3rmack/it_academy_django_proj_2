from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^hello_world/$', views.link_hello_world, name='hello_world'),
    url(r'^hello_earth/$', views.link_hello_earth, name='hello_earth'),
    url(r'^hello_universe/$', views.link_hello_universe, name='hello_universe'),
    url(r'^$', views.index),
]