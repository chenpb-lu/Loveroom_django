"""
file：myfilter.py
author：陈先生
date：2019/8/1619:58
blog:https://chenpb-lu.github.io
"""
from django.conf import settings
from django import template
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

