"""it_academy_django_proj_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^homework2/', include('homework2.urls')),
    url(r'^homework3/', include('homework3.urls')),
    url(r'^homework4/', include('homework4.urls')),
    url(r'^homework5/', include('homework5.urls')),
    url(r'^homework6/', include('homework6.urls')),
    url(r'^admin/', admin.site.urls),
]
