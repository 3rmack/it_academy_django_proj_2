from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'data_form$', views.data_form, name='data_form'),
    url(r'search_form$', views.search_form, name='search_form'),
    url(r'data_form_post$', views.data_form_post, name='data_form_post'),
    url(r'search_form_post$', views.search_form_post, name='search_form_post'),

]
