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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    url(r'^cpb/$', views.cpb, name='cpb'),
    url(r"^search/$",views.search,name='search'),
    url(r'^collection/(?P<id>\d+)/$',views.HouseCollections.as_view(),name='house_collection'),
    url(r'^change_avator/$', views.ChangeAvator.as_view(), name='change_avator'),

]
