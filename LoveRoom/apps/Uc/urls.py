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
    url(r'^register/$',views.Register.as_view(), name='register'),
    url(r'^phonelogin/$',views.PhoneLogin.as_view(),name='phonelogin'),
    url(r'^pwlogin/$',views.PwLogin.as_view(),name='pwlogin'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^change_passwd/$',views.change_passwd,name="change_passwd"),
    url(r'^profile/$',views.ProfileView.as_view(),name="profile"),
    url(r'^collect/$',views.Collect.as_view(),name="collect")

]
