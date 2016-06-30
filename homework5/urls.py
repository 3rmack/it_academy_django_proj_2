from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'view_workers$', views.view_workers, name='view_workers'),
    url(r'add_worker$', views.add_worker, name='add_worker'),
    url(r'view_equipment$', views.view_equipment, name='view_equipment'),
    url(r'add_equipment$', views.add_equipment, name='add_equipment'),
]
