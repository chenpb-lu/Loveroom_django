"""
file：myfilter.py
author：陈先生
date：2019/8/1619:58
blog:https://chenpb-lu.github.io
"""
from django.conf import settings
from django import template
from apps.show.models import MetaInconfont
import json

register = template.Library()

@register.filter
def get_img_url(value):
    try:
        jsonobj =json.loads(value)
        a = jsonobj[0]['photo_url']
        return settings.MEDIA_URL+a
    except:
        return value


@register.filter
def limit_title(value):
    try:
        if  len(value) > 12:
            return value[:12] + " ..."
        else:
            return value
    except:
        return value

@register.filter
def contrast(value,arg):
    if int(value) < int(arg):
        return True
    else:
        return False

@register.filter
def price(value):
    return int(value/100)

@register.filter
def jsonvalue(value,arg):
    a = json.loads(value)
    return a[arg]

@register.filter
def housetype(value):
    type = value['type']
    info = json.loads(value['info'])
    if type == 0:
        return f"整套·{info['layoutWc']}居室"
    elif type == 1:
        return f"单间·{info['layoutWc']}居室"
    elif type == 2:
        return f"床位{info['bedCount']}个"


@register.filter
def get_img_len(value,arg):
    try:
        lit = []
        if arg != '0':
            jsonobj =json.loads(value)
            i = 0
            while i < len(jsonobj):
                lit.append(i)
                i += 1
        else:
            lit = [0,1,2,3,4]
        return lit
    except:
        return value

@register.filter
def get_img(value,arg):
    try:
        jsonobj =json.loads(value)
        a = jsonobj[int(arg)]['photo_url']
        return settings.MEDIA_URL+a
    except:
        return value

@register.filter
def house_detail_show(value,arg):
    try:
        if arg == "type":
            if value == 0:
                return "整套房源"
            elif value == 1:
                return "单个房间"
            elif value == 2 :
                return "合住房间"
        else:
            jsonobj = json.loads(value)
            ret = jsonobj[arg]
            if ret:
                return ret
            elif ret == 0:
                return 0
            else:
                return "暂无信息"
    except:
        return value

@register.filter
def house_description_show(value,arg):
    try:
        jsonobj = json.loads(value)
        if arg == 'curDayBookingTime':
            if jsonobj[arg] :
                return jsonobj[arg]
            else:
                return "随时"
        elif arg == "maxBookingDays":
            if jsonobj[arg] :
                return f"{jsonobj[arg]}天"
            else:
                return "随时可预订"
        elif arg == "additionalChargePerGuest":
            return int(jsonobj[arg]/100)
        return jsonobj[arg]

    except:
        return value


@register.filter
def metafont(value):
    try:
        classname = MetaInconfont.objects.filter(metaId=value)[0].classname
        return classname
    except:
        return value

@register.filter
def limit(value):
    try:
        jsonobj = json.loads(value)
        return jsonobj
    except:
        return value