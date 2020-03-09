from django.shortcuts import render, HttpResponse,redirect,reverse
from django.http import JsonResponse
from io import BytesIO
import os
import time
import datetime
from LoveRoom.settings import MEDIA_ROOT, MEDIA_URL

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

class ChangeAvator(LoginRequiredMixin, View):
    def post(self, request):
        today = datetime.date.today().strftime("%Y%m%d")
        # 图片的data-img格式=>data:image/jpg;base64,xxxx
        img_src_str = request.POST.get("image")
        img_str = img_src_str.split(',')[1]
        # 取出格式:jpg/png...
        img_type = img_src_str.split(';')[0].split('/')[1]
        # 取出数据:转化为bytes格式
        img_data = base64.b64decode(img_str)
        # 相对上传路径: 头像上传的相对路径
        avator_path = os.path.join("avator",today)
        # 绝对上传路径：头像上传的绝对路径
        avator_path_full = os.path.join(MEDIA_ROOT, avator_path)
        if not os.path.exists(avator_path_full):
            os.mkdir(avator_path_full)
        filename = str(time.time())+"."+img_type
        # 绝对文件路径，用于保存图片
        filename_full = os.path.join(avator_path_full, filename)
        # 相对MEDIA_URL路径，用于展示数据
        img_url = f"{MEDIA_URL}{avator_path}/{filename}"
        try:
            with open(filename_full, 'wb') as fp:
                fp.write(img_data)
            ret = {
                "result": "ok",
                "file": img_url
            }
        except Exception as ex:
            ret = {
                "result": "error",
                "file": "upload fail"
            }

        request.user.avator_sor = os.path.join(avator_path,filename)
        request.user.save()
        return JsonResponse(ret)
