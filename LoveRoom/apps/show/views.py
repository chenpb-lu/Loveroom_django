from django.shortcuts import render
from django.views.generic import View
from apps.house.models import HouseInfo,SiteInfo
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
import json
import datetime
# Create your views here.
class showDetail(View):
    def get(self,request):
        houselist = HouseInfo.objects.all().values('id','title','photo','price','info','type','location')
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
        }
        return render(request,"house/properties-list.html",kwag)

def test(request):

    city = request.GET.get('city')
    district = request.GET.get('district')
    st = request.GET.get('st')
    et = request.GET.get('et')
    type = request.GET.get('type')
    #还有加上没有时间的情况
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
    }

    return render(request,"show/mycale.html",kwag)