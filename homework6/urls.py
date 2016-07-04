from django.conf.urls import url
from. import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add_article', views.add_article, name='add_article'),
    url(r'add_section', views.add_section, name='add_section'),
    url(r'add_connections', views.add_connections, name='add_connections'),
    url(r'articles', views.view_articles, name='view_articles'),
    url(r'sections', views.view_sections, name='view_sections'),
    url(r'connections', views.view_connections, name='view_connections'),
]
