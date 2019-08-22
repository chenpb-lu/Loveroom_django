"""
file：gethouseinfo.py
author：陈先生
date：2019/8/1422:29
blog:https://chenpb-lu.github.io
"""
import LoveRoom.urls
import requests
import re
import json
from apps.house.models import City,SiteInfo,HouseInfo
import os
from bs4 import BeautifulSoup

# dis_url = "https://www.zhenguo.com/changsha/d430102/"


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'__mta=251008697.1563436089942.1566438866676.1566459043037.37; uuid=1D5E3EDE0AA6606D1280CCCC139C3E8FEF846985847A37FC8026BC4EC634A51A; _lxsdk_cuid=16c040d804ac8-0a3fd62f515e97-1571466f-1fa400-16c040d804bc8; _lxsdk=1D5E3EDE0AA6606D1280CCCC139C3E8FEF846985847A37FC8026BC4EC634A51A; never-show-xcxh=1; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; __mta=251008697.1563436089942.1566352463109.1566444587225.36; zgwww=6295f570-a930-11e9-b1c4-e39b01391dd1; XSRF-TOKEN=S2YwwyiY-hK0QNHoe5f3rq6dtHWBAIknCKdE; _ga=GA1.2.774742589.1563436089; _gid=GA1.2.1724521718.1565927689; _lxsdk_s=16cb858f39a-18a-765-40e%7C2537929755%7C1',
    'Host':'www.zhenguo.com',
    'Referer':'https://www.zhenguo.com/changsha/?dateBegin=20190822&dateEnd=20190823',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
# house_root = "https://www.zhenguo.com"
# ret = requests.get(dis_url,headers=headers).text
# pg_num = int(re.findall(r'<a class="page-link".*>(\d+)</a>',ret)[0])
# if pg_num > 5:
#     pg_num = 5
# count = 0
# for num in range(1,pg_num+1):
#     tem_url = dis_url + f"pn{num}"
#     html = requests.get(tem_url,headers=headers).text
#     soup = BeautifulSoup(html,'lxml')
#     href_list = soup.find_all('a',class_='product-card product-card--has-avatar product-card--has-tags')
#     for a in href_list:
#         house_path = a["href"]
#         house_url = house_root + house_path
#         ret = requests.get(house_url,headers=headers).text
#         info = re.findall(r'r-props-J-gallery">(.*)</scr',ret)
#         info = info[0].strip("<>!-")
#         houseinfo = json.loads(info)
#         product = houseinfo["product"]
#
#         # 房子类型
#         rentType = product["rentType"]
#         # 位置详情
#         address = product["addressInfo"]
#         address["locationArea"] = product["locationArea"]
#         # 行政区
#         distritName = address["districtName"]
#         siteinfo = SiteInfo.objects.filter(name=distritName)[0]
#         # 城市
#         cityid = siteinfo.city_id
#         #标题
#         title = product["title"]
#         # 商圈
#         locationArea = product["locationArea"]
#         area = SiteInfo.objects.filter(name=locationArea,type=7)[0]
#         # 房子详情
#         if "liveWithOwner" in product:
#             liveWithOwner = product["liveWithOwner"]
#         else:
#             liveWithOwner = 0
#         housedetail = {
#             'productType' : product["productType"],
#             "layoutRoom" : product["layoutRoom"],
#             "rentLayoutRoom" : product["rentLayoutRoom"],
#             "layoutHall" : product["layoutHall"],
#             "layoutKitchen" : product["layoutKitchen"],
#             "layoutWc" : product["layoutWc"],
#             "bedCount" : product["bedCount"],
#             "wcType" : product["wcType"],
#             "usableArea" : product["usableArea"],
#             "maxGuestNumber":product["maxGuestNumber"],
#             "liveWithOwner" : liveWithOwner
#         }
#
#
#         # 房子介绍
#         if "detailIntroduction" in product:
#             detailIntroduction = product["detailIntroduction"]
#         else:
#             detailIntroduction = ''
#
#         if "aroundInfo" in product:
#             aroundInfo = product["aroundInfo"]
#         else:
#             aroundInfo = ''
#         introduce = {
#             "description":product["description"],
#             "detailIntroduction":detailIntroduction,
#             "aroundInfo":aroundInfo
#         }
#
#         # 房客须知
#         guestNoticeList = product["guestNoticeList"]
#
#         # 自动回复
#         if "hostMessage" in product:
#             hostMessage = product["hostMessage"]
#         else:
#             hostMessage = ''
#
#         # 普通价格
#         price = product["price"]
#
#         # 节假日价格
#         h_price = price + price*0.5
#
#         # 房子设施
#         facility = {'bedList':product['bedList'], "metaGroups":product["metaGroups"]}
#
#         # 预订设置
#         productRpInfo = product['productRpInfo']
#         if "cleanPrice" in productRpInfo:
#             cleanPrice = productRpInfo["cleanPrice"]
#         else:
#             cleanPrice = 0
#         book = {"minBookingDays":productRpInfo["minBookingDays"], "maxBookingDays":productRpInfo["maxBookingDays"], "curDayBookingTimeCode":productRpInfo["curDayBookingTimeCode"],
#                 "curDayBookingTime":productRpInfo["curDayBookingTime"], "earliestCheckinTimeCode":productRpInfo["earliestCheckinTimeCode"],
#                 "earliestCheckinTime":productRpInfo["earliestCheckinTime"], "latestCheckinTimeCode":productRpInfo["latestCheckinTimeCode"],
#                 "latestCheckinTime":productRpInfo['latestCheckinTime'], "latestCheckoutTimeCode":productRpInfo["latestCheckoutTimeCode"],
#                 "latestCheckoutTime":productRpInfo["latestCheckoutTime"], "maxCheckinGuests":productRpInfo["maxCheckinGuests"],
#                 "maxAdditionalGuests":productRpInfo["maxAdditionalGuests"],"moveupCancelDays":productRpInfo["moveupCancelDays"],
#                 "moveupCancelTime":productRpInfo["moveupCancelTime"], "deductType":productRpInfo["deductType"], "deductRate":productRpInfo["deductRate"],
#                 "additionalChargePerGuest":productRpInfo["additionalChargePerGuest"], "cleanPrice":cleanPrice}
#
#         # 照片
#         photolist = product['productMediaInfoList']
#         housephotolist = []
#         for photo in photolist:
#             mediaCategory = photo['mediaCategory']
#             photo_url = photo['mediaUrl']
#             isCover = photo['isCover']
#             categoryName = photo['categoryName']
#             img = requests.get(photo_url, headers=headers)
#             imgname = photo_url.split('/')[-1]
#             img_path = f"../media/house/{imgname}"
#             if not os.path.exists(img_path):
#                 with open(img_path, 'wb') as f:
#                     f.write(img.content)
#             housephotolist.append({
#                 'photoCategory' : mediaCategory, 'photo_url' : f'house/{imgname}',
#                 'isCover' : isCover, 'categoryName':categoryName
#             })
#
#
#         try:
#             address = json.dumps(address)
#             housedetail = json.dumps(housedetail)
#             introduce = json.dumps(introduce)
#             guestNoticeList = json.dumps(guestNoticeList)
#             facility = json.dumps(facility)
#             book = json.dumps(book)
#             housephotolist = json.dumps(housephotolist)
#             HouseInfo.objects.get_or_create(city_id=cityid, district_id=siteinfo.id, type=rentType, title=title,
#                                             area=area.id,limit=guestNoticeList, auto_reply=hostMessage, price=price, h_price=h_price,
#                                             info=housedetail, introduce=introduce, facility=facility, book=book,
#                                             photo=housephotolist, location=address, owner_id=8)
#             count += 1
#             print(f"第{count}间完成")
#         except Exception as e:
#             print(e)










"""
        
        "rentType":1, 出租类型  0：整套房源  1：独立房间 2：合住房间
        "productType":0, 房源类型  未明确
        "layoutRoom":1 室
        "rentLayoutRoom":1,室（租）
        "layoutHall":0,厅
        "layoutKitchen":0,厨
        "layoutWc":1,卫生间
        "usableArea":"20",大小
        "bedCount":2,
        "wcType":0, 厕所类型  0 独卫 1 公
        "title":"从前慢客栈 山水湾 MC 影城对面 龙塘小区投影双床房",  标题
        "description":[
            "步步高，MC影城对面，紧挨保利国际，湖南工程学院贺龙校，周边交通便利。" 亮点
        ],
        "detailIntroduction":"大屏投影，五星床品，卫生清洁，欢迎入住体验", 介绍 选
        "aroundInfo": 选
        "liveWithOwner":0,
        "maxGuestNumber":4, 最多住几人
        "addNumber":0
        "cleanPrice":0
        "locationArea":"城西安置小区",
        "productMediaInfoList"：图片
        "cityName":"长沙",
        "districtName":"长沙县",
        "fullAddress":"长沙长沙县万家丽北路龙塘小区"
        "longitude":113.054707,
        "latitude":28.265053
        "price":19800,
        "additionalChargePerGuest":0, 家人加钱
        "isNeedCleanPrice":0,是否有清洁费
        
        "bookingType":0,
        "minBookingDays":1,
        "maxBookingDays":0,
        "curDayBookingTimeCode":"00:00-24:00_0_0",
        "curDayBookingTime":"",
        "earliestCheckinTimeCode":"12:00_0_2",
        "earliestCheckinTime":"12:00"
        "latestCheckinTimeCode":"1:00_1_1",
        "latestCheckinTime":"次日1:00", 最晚入住
        "latestCheckoutTimeCode":"12:00_0_1",
        "latestCheckoutTime":"12:00",
        "moveupCancelDays":1,
        "moveupCancelTime":"12:00",
        "deductType":"【宽松】入住前1天12:00前退订，可获100%退款。之后退订不退款",
        "deductRate":10000,
        "cityId":430100,
        productMediaInfoList
        "bedList":Array[1],
        "metaGroups
        guestNoticeList
        
"""
from apps.show.models import MetaInconfont
ret = requests.get("https://www.zhenguo.com/housing/1570604/",headers=headers).text
print(ret)
info = re.findall(r'r-props-J-gallery">(.*)</scr',ret)
print(info)
info = info[0].strip("<>!-")
jsonobj = json.loads(info)
f = jsonobj['product']


# for item in f["facilityList"]:
#     MetaInconfont.objects.get_or_create(metaId=item['metaId'],value=item['value'])
#
# for item in f["roomServiceList"]:
#     MetaInconfont.objects.get_or_create(metaId=item['metaId'], value=item['value'])
