from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'city_form$', views.city_form, name='city_form'),
    url(r'city_form_post$', views.city_form_post, name='city_form_post'),
    url(r'street_form$', views.street_form, name='street_form'),
    url(r'street_form_post$', views.street_form_post, name='street_form_post'),
    url(r'search_form$', views.search_form, name='search_form'),
    # url(r'search_form_post$', views.search_form_post, name='search_form_post'),

]
