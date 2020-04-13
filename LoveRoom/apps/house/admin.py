from django.contrib import admin
from .models import Order_date,Order, HouseInfo, SiteInfo, City

# Register your models here.
admin.site.register(Order_date)
admin.site.register(Order)
admin.site.register(HouseInfo)
admin.site.register(SiteInfo)
admin.site.register(City)