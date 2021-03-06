"""testp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from testp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chart/?$', TemplateView.as_view(template_name = "chart1.html")),
    url(r'^chart2/?', TemplateView.as_view(template_name = "chart2.html")),
    url(r'^marital_data/?', views.get_marital_json),
    url(r'^industry_data/?', views.get_industry_json),
    url(r'^index/', TemplateView.as_view(template_name = "index.html")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
