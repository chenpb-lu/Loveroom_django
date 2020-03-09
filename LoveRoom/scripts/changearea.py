"""
file：changearea.py
author：陈先生
date：2019/8/2114:22
blog:https://chenpb-lu.github.io
"""
import LoveRoom.urls
from apps.house.models import SiteInfo, HouseInfo
# houselist = HouseInfo.objects.all()
#
# for item in houselist:
#     area = item.area
#     site = SiteInfo.objects.filter(id=area)[0]
#     house_city = item.city_id
#     site_city = site.city_id
#     site_type = site.type
#     site_name = site.name
#     if site_type != 7 or site_city != house_city:
#         area_id = SiteInfo.objects.filter(name=site_name,type=7,city_id=house_city)[0].id
#         house = HouseInfo.objects.get(id=item.id)
#         house.area = area_id
#         house.save()
#         print(f"{item.id}ok")




