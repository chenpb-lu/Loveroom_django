from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from apps.house.models import HouseInfo,SiteInfo,City
from apps.show.models import HouseCollection
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

class LoginRequiredMixin(object):
    """
    登陆限定，并指定登陆url
    """
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url='/')



class showDetail(View):
    def get(self,request):
        city = request.GET.get('city')
        district = request.GET.get('district')
        st = request.GET.get('st')
        et = request.GET.get('et')
        type = request.GET.get('type')
        minprice = request.GET.get('minprice')
        maxprice = request.GET.get('maxprice')
        collection = []
        if request.user.id:
            user_id = request.user.id
            collection = HouseCollection.objects.filter(user_id=user_id,status=True).values('house_id')

        if not city:
            city = "长沙"
        city_id = City.objects.filter(name=city)
        if not city_id:
            city_id = City.objects.filter(name=(city + "市"))

        city_id = city_id[0].id
        houselist = HouseInfo.objects.filter(city_id=city_id).values('id', 'title', 'photo', 'price', 'info',
                                                                     'type', 'location', 'district_id','area')

        if type:
            houselist = houselist.filter(type=type)
        if district:
            district_id = SiteInfo.objects.filter(name=district)[0]
            if district_id.type == 0:
                houselist = houselist.filter(district_id=district_id.id)
            else:
                district_id = SiteInfo.objects.filter(name=district,type=7,city_id=city_id)[0]
                houselist = houselist.filter(area=district_id.id)

        if minprice:
            minprice_b = int(minprice)*100
            # print(minprice_b)
            houselist = houselist.filter(price__gt=minprice_b)
        if maxprice:
            maxprice_b = int(maxprice)*100
            # print(maxprice)
            houselist = houselist.filter(price__lt=maxprice_b)
        # else:
        #     houselist = []

        if not st and not et:
            now = datetime.datetime.now()
            delta = datetime.timedelta(days=1)
            n_days = now + delta
            st = now.strftime('%m/%d/%Y')
            et = n_days.strftime('%m/%d/%Y')
        districtlist = SiteInfo.objects.filter(cityname=city, type=0).values('name', 'id')
        arealist = SiteInfo.objects.filter(cityname=city, type=7).values('name', 'id')
        houselist = houselist.order_by('id')
        paginator = Paginator(houselist, 12)
        page = request.GET.get('page')
        numlist = []
        if paginator.num_pages > 5 :
            numlist = ['1','2','3','4','5']
        else:
            for i in range(1,paginator.num_pages + 1):
                numlist.append(str(i))
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
            page = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        kwag = {
            "houselist" : contacts,
            'page' : page,
            'fivenum':numlist,
            'pagenum':paginator.num_pages,
            'districtlist': districtlist,
            'city': city,
            'arealist': arealist,
            "district": district,
            'st': st,
            'et': et,
            'type': type,
            'minprice': minprice,
            'maxprice': maxprice,
            'collection' :collection
        }
        return render(request,"house/properties-list.html",kwag)


def test(request):

    city = request.GET.get('city')
    district = request.GET.get('district')
    st = request.GET.get('st')
    et = request.GET.get('et')
    type = request.GET.get('type')
    minprice = request.GET.get('minprice')
    maxprice = request.GET.get('maxprice')
    if not city:
        city = "长沙"
    if not st and not et :
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=1)
        n_days = now + delta
        st = now.strftime('%m/%d/%Y')
        et = n_days.strftime('%m/%d/%Y')
    districtlist = SiteInfo.objects.filter(cityname=city,type=0).values('name','id')
    arealist = SiteInfo.objects.filter(cityname=city,type=7).values('name','id')
    kwag = {
        'districtlist' : districtlist,
        'city': city,
        'arealist' : arealist,
        "district": district,
        'st' : st,
        'et' : et,
        'type' : type,
        'minprice' : minprice,
        'maxprice' : maxprice,
    }

    return render(request, "show/submit.html", kwag)

def house_detail(request,id):
    house = HouseInfo.objects.filter(id=id)[0]
    st = request.GET.get('st')
    et = request.GET.get('et')
    kwag = {
        'house': house,
        'st' : st,
        'et' : et,
    }
    return render(request,'show/housedetail.html',kwag)

class Booking(LoginRequiredMixin,View):
    def get(self,request,id):
        house = HouseInfo.objects.filter(id=id)[0]
        st = request.GET.get('st')
        et = request.GET.get('et')
        kwag = {
            'house': house,
            'st': st,
            'et': et,
        }
        return render(request,'show/booking.html',kwag)

