from django.shortcuts import render, HttpResponse,redirect,reverse
from django.http import JsonResponse
from io import BytesIO
import base64
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from libs import sms
import logging
from django.contrib import  auth
from django.contrib.auth.decorators import login_required
from apps.house.models import SiteInfo,HouseInfo
from apps.show.models import HouseCollection
from django.forms.models import model_to_dict

logger = logging.getLogger('apis')
import random

def get_mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        mobile = request.GET.get("mobile")
        if mobile is None: raise ValueError("手机号不能为空！")
        mobile_captcha = "".join(random.choices('0123456789', k=6))
        from django.core.cache import cache
        # 将短信验证码写入redis, 300s 过期
        cache.set(mobile, mobile_captcha, 300)
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        logger.error(ex)
        ret = {"code": 400, "msg": "验证码发送失败！"}
    return JsonResponse(ret)

def cpb(request):
    ret = {"测试内容":400}
    return JsonResponse(ret)


def search(request):
    city = request.GET.get('city')
    print(city)
    if not city:
        city = "长沙"
    district = SiteInfo.objects.filter(cityname=city, type=0).values('name')
    print(district)
    kwag = {
        'district': district,
        'city' : city
    }
    return render(request, "show/submit.html", kwag)

class LoginRequiredMixin(object):
    """
    登陆限定，并指定登陆url
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/')

class HouseCollections(LoginRequiredMixin,View):
    def get(self,request,id):
        house = HouseInfo.objects.get(id=id)
        result = HouseCollection.objects.get_or_create(user=request.user,house=house)
        house_collection = result[0]
        if not result[1]:
            if house_collection.status :
                house_collection.status = False
            else:
                house_collection = True
        house_collection.save()
        msg = model_to_dict(house_collection)
        ret_info = {"code": 200, "msg": msg}
        return JsonResponse(ret_info)
