"""LoveRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from apps.house import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^house/',include('apps.house.urls',namespace='house')),
    url(r'^uc/',include('apps.Uc.urls', namespace='uc')),
    url(r'^apis/', include('apps.apis.urls', namespace="apis")),
    url(r'^$',views.index)
]


# meida 处理
from . import settings
if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',  serve, {"document_root": settings.MEDIA_ROOT}),
    ]