from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.first_form),
    url(r'^first_form_post', views.first_form_post),
    url(r'^second_form_post', views.second_form_post)
]
