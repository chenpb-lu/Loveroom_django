"""
file：getcitydata.py
author：陈先生
date：2019/8/1221:04
blog:https://chenpb-lu.github.io
"""

import LoveRoom.urls
import requests
import re
import json
from apps.house.models import SiteInfo
from apps.house.models import City
import urllib



url = "http://www.jsycyz.cn/n2373c18.aspx"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
ret = requests.get(url,headers=headers).text
cityids = re.findall(r'\(([\d]{6})\)</TD',ret)
cpb = []
for i in range(len(cityids)):

    tem = cityids[i]
    if tem[-3:] == "000":
        tem2 = tem[:3]
        cpb.append(tem2+'100')
    else:
        if tem not in cpb:
            cpb.append(tem)


print(cpb)


url = "https://www.zhenguo.com/api/phx/cprod/locations?cityId="

# for i in cpb:
#     t_url = url + i
#     request = urllib.request.Request(url=t_url, headers=headers)
#     json_text = urllib.request.urlopen(request).read().decode()
#     obj = json.loads(json_text)
#     data = obj["data"]
#     lis= data["listings"]
#     cityname = lis['l'][0]['cityName']
#     cityn = lis['l'][0]['cityName']+ '市'
#     city = City.objects.filter(name=cityn)[0]
#     for i in lis['l']:
#         type = i['type']
#         pinyin = i['pinyin']
#         name = i['name']
#         radius = i['radius']
#         latitude = i['latitude']
#         longitude =i['longitude']
#         SiteInfo.objects.create(city_id=city.id,type=type,pinyin=pinyin,name=name,radius=radius,latitude=latitude,longitude=longitude,cityname=cityname)
#     for j in lis['a']:
#
#         type = 7
#         pinyin = j['pinyin']
#         name = j['name']
#         latitude = j['latitude']
#         longitude = j['longitude']
#         SiteInfo.objects.create(city_id=city.id, type=type, pinyin=pinyin, name=name,
#                                 latitude=latitude, longitude=longitude,cityname=cityname)
#     for k in lis['d']:
#
#         name = k['name']
#         pinyin = k['pinyin']
#         type = 0
#         SiteInfo.objects.create(city_id=city.id, type=type, pinyin=pinyin, name=name,cityname=cityname)
#     print(f"{count}-{cityn}完毕")
#     count += 1
#
#     """
#     l:LANDMARK 地标
#     a:AREA 区域 商圈
#     d:DISTRICT 行政区
#
#     type ：
#     0：行政区
#     1：高校
#     2：火车站
#     3：景点
#     4：机场
#     5：医院
#     6：购物广场
#     7：商圈
#
#     """
#     """
#     id = models.CharField(verbose_name="地点id",max_length=11,primary_key=True)
#     city = models.ForeignKey('City',max_length=11,verbose_name="城市")
#     type = models.IntegerField(choices=SITE_TYPE,verbose_name="地点类型")
#     pinyin = models.CharField(verbose_name="拼音",max_length=100)
#     name = models.CharField(verbose_name="地点名称",max_length=100)
#     radius = models.IntegerField(verbose_name="范围")
#     latitude = models.IntegerField(verbose_name="维度")
#     longitude = models.IntegerField(verbose_name="经度")
#     """

count = 1


for i in range(0,len(cpb)):
    t_url = url + cpb[i]
    request = urllib.request.Request(url=t_url, headers=headers)
    json_text = urllib.request.urlopen(request).read().decode()
    obj = json.loads(json_text)
    data = obj["data"]
    lis= data["listings"]
    try:
        cityname = lis['l'][0]['cityName']
        cityn = lis['l'][0]['cityName'] + '市'
        city_q = City.objects.filter(name=cityn)
        if not city_q:
            city_q = City.objects.filter(name=cityname)
            if not city_q:
                continue
        city = city_q[0]
        for i in lis['l']:
            type = i['type']
            pinyin = i['pinyin']
            name = i['name']
            radius = i['radius']
            latitude = i['latitude']
            longitude = i['longitude']
            SiteInfo.objects.create(city_id=city.id, type=type, pinyin=pinyin, name=name, radius=radius,
                                    latitude=latitude, longitude=longitude, cityname=cityname)
        for j in lis['a']:
            type = 7
            pinyin = j['pinyin']
            name = j['name']
            latitude = j['latitude']
            longitude = j['longitude']
            SiteInfo.objects.create(city_id=city.id, type=type, pinyin=pinyin, name=name,
                                    latitude=latitude, longitude=longitude, cityname=cityname)
        for k in lis['d']:
            name = k['name']
            pinyin = k['pinyin']
            type = 0
            SiteInfo.objects.create(city_id=city.id, type=type, pinyin=pinyin, name=name, cityname=cityname)
        print(f"{count}-{cityn}完毕")
        count += 1
    except:
        pass



