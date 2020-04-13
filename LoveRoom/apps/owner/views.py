from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
from apps.house.models import City, SiteInfo, HouseInfo
from apps.Uc.models import User
import json

class LoginRequiredMixin(object):
    """
    登陆限定，并指定登陆url
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/')

# Create your views here.
class Create(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'owner/create.html')

    def post(self,request):
        try:
            data = {}
            concat = request.POST
            dicts = dict(concat)
            facility = {'bedList': [], 'metaGroups': [{'id': 0, 'name': '设施', 'group': []},
                                                              {'id': 1, 'name': '电器', 'group': []},
                                                              {'id': 2, 'name': '卫浴', 'group': []},
                                                              {'id': 3, 'name': '厨房', 'group': []},
                                                              {'id': 4, 'name': '客房服务', 'group': []}]}
            limit = [{
                    "metaId":46,
                    "type":6,
                    "value":"允许抽烟",
                    "fillType":0,
                    "metaValue":"0"
                },
                {
                    "metaId":51,
                    "type":6,
                    "value":"适合婴幼儿（2岁以下）",
                    "fillType":0,
                    "metaValue":"0"
                },
                {
                    "metaId":47,
                    "type":6,
                    "value":"允许聚会",
                    "fillType":0,
                    "metaValue":"0"
                },
                {
                    "metaId":50,
                    "type":6,
                    "value":"适合儿童（2-12岁）",
                    "fillType":0,
                    "metaValue":"0"
                },
                {
                    "metaId":48,
                    "type":6,
                    "value":"允许做饭",
                    "fillType":0,
                    "metaValue":"0"
                },
                {
                    "metaId":53,
                    "type":6,
                    "value":"其他注意事项",
                    "fillType":1,
                    "metaValue":""
                },
                {
                    "metaId":52,
                    "type":6,
                    "value":"适合老人（60岁以上）",
                    "fillType":0,
                    "metaValue":"0"
                },
                {
                    "metaId":49,
                    "type":6,
                    "value":"允许携带宠物",
                    "fillType":0,
                    "metaValue":"0"
                }]

            for key, vuale in dicts.items():
                if 'metaid' in key and vuale[0]:
                    meta_info = vuale[0].split('-')
                    group = int(meta_info[0])
                    facility['metaGroups'][group]['group'].append({
                        "metaId": int(meta_info[1]),
                        "metaValue": 1,
                        "value": meta_info[2]
                    })
                elif 'xuzhi' in key and vuale[0]:
                    limit_info = vuale[0].split('-')
                    limit[int(limit_info[1])]["metaValue"] = limit_info[0]

            limit[5]["metaValue"] = concat.get('other_note')
            data['limit'] = json.dumps(limit)
            print(0)
            city = City.objects.get(name=concat.get('city_name') + "市")
            data['city'] = city
            district = SiteInfo.objects.get(name=concat.get('district'))
            data['district'] = district
            user = User.objects.get(id=request.user.id)
            data['owner'] = user
            area = SiteInfo.objects.filter(name=concat.get('area_name'), city_id=city.id)[0]
            data['area'] = area.id
            house_type = concat.get('house_type')
            if house_type == "整套房源":
                data['type'] = 0
            elif house_type == "独立房间":
                data['type'] = 1
            else:
                data['type'] = 2
            print(00)
            data['title'] = concat.get('house_title')
            introduce = {}
            introduce['description'] = concat.get('description')
            introduce['detailIntroduction'] = concat.get('detailIntroduction')
            introduce['aroundInfo'] = concat.get('aroundInfo')
            data['introduce'] = json.dumps(introduce)

            if concat.get('tatami'):
                facility['bedList'].append({"metaId": 44, "type": 5, "value": "榻榻米", "fillType": 0,
                                                    "metaValue": concat.get('tatami')})

            if concat.get('sxp'):
                facility['bedList'].append({"metaId": 42, "type": 5, "value": "上下铺", "fillType": 0,
                                                    "metaValue": concat.get('sxp')})

            if concat.get('twobed'):
                facility['bedList'].append({"metaId": 40, "type": 5, "value": "双人床", "fillType": 0,
                                                    "metaValue": concat.get('twobed')})

            if concat.get('bigtwobed'):
                facility['bedList'].append({"metaId": 39, "type": 5, "value": "双人床", "fillType": 0,
                                                    "metaValue": concat.get('bigtwobed')})

            data['facility'] = json.dumps(facility)

            info = {"productType": 11, "layoutRoom": 0, "rentLayoutRoom": 0, "layoutHall": 0,
                    "layoutKitchen": 0,"layoutWc": 0, "bedCount": 0, "wcType": 0, "usableArea": "0", "maxGuestNumber": 0, "liveWithOwner": 0}

            info['layoutRoom'] = int(concat.get('layoutRoom'))
            info['rentLayoutRoom'] = int(concat.get('layoutRoom'))
            info['layoutHall'] = int(concat.get('layoutHall'))
            info['layoutKitchen'] = int(concat.get('layoutKitchen'))
            info['layoutWc'] = int(concat.get('layoutWc'))
            info['bedCount'] = int(concat.get('bedCount'))
            info['usableArea'] = concat.get('usableArea')
            info['maxGuestNumber'] = int(concat.get('guest_num'))
            data['info'] = json.dumps(info)
            print(1)
            book = {"minBookingDays":1,
                    "maxBookingDays":0,
                    "curDayBookingTimeCode":"24:00_0_1",
                    "curDayBookingTime":"24:00前可订当天",
                    "earliestCheckinTimeCode":"14:00_0_2",
                    "earliestCheckinTime":"14:00",
                    "latestCheckinTimeCode":"24:00_0_1",
                    "latestCheckinTime":"24:00",
                    "latestCheckoutTimeCode":"12:00_0_1",
                    "latestCheckoutTime":"12:00",
                    "maxCheckinGuests":10,
                    "maxAdditionalGuests":0,
                    "moveupCancelDays":7,
                    "moveupCancelTime":"12:00",
                    "deductType":"【严格】入住的前7天12:00前退订，可获50%退款。之后退订不退款",
                    "deductRate":5000,
                    "additionalChargePerGuest":0,
                    "cleanPrice":0
                            }
            book['earliestCheckinTime'] = concat.get('in_time')
            book['latestCheckoutTime'] = concat.get('out_time')
            data['book'] = json.dumps(book)

            location = {"longitude":113.042358,"latitude":28.186494,}

            location['cityName'] = concat.get('city_name')
            location['districtName'] = concat.get('district')
            location['areaID'] = area.id
            location['locationArea'] = concat.get('area_name')
            location['fullAddress'] = concat.get('address')
            data['location'] = json.dumps(location)

            data['price'] = int(concat.get('price')) * 100
            data['h_price'] = int(concat.get('h_price')) * 100
            print(2)
            photo = [{
                                "photoCategory":0,
                                "photo_url":"house/notphoto.png",
                                "isCover":1,
                                "categoryName":"封面"
                            },
                            {
                                "photoCategory": 1,
                                "photo_url": "house/notphoto.png",
                                "isCover": 0,
                                "categoryName": "其他"
                            },
                            ]
            data['photo'] = json.dumps(photo)
            print(3)
            HouseInfo.objects.update_or_create(**data)


            return JsonResponse({"code": 200, "msg": "123"})
        except Exception as e:
            print(str(e))
            return JsonResponse({"code": 500, "msg": str(e)})
