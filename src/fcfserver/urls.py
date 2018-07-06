"""fcfserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import re_path, include
from django.contrib import admin
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="FCF Server API")

urlpatterns = [
    path(r'admin/', admin.site.urls),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^', include('football.urls')),
    re_path(r'^schema/$', schema_view),
]
