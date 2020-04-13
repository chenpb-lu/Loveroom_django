from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(verbose_name="城市名称",max_length=32)
    pid = models.ForeignKey('City',max_length=11,null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class SiteInfo(models.Model):
    city = models.ForeignKey('City',max_length=11,verbose_name="城市")
    SITE_TYPE = (
        (0, '行政区'),
        (1, '高校'),
        (2, '火车站'),
        (3, '景点'),
        (4, '机场'),
        (5, '医院'),
        (6, '购物广场'),
        (7, '商圈'),
    )
    type = models.IntegerField(choices=SITE_TYPE,verbose_name="地点类型")
    pinyin = models.CharField(verbose_name="拼音",max_length=100)
    name = models.CharField(verbose_name="地点名称",max_length=100)
    radius = models.IntegerField(verbose_name="范围",null=True)
    latitude = models.IntegerField(verbose_name="维度",null=True)
    longitude = models.IntegerField(verbose_name="经度",null=True)
    cityname = models.CharField(verbose_name="城市名称",max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


from apps.Uc.models import User
class HouseInfo(models.Model):
    city = models.ForeignKey(City,max_length=11,verbose_name="城市")
    district = models.ForeignKey(SiteInfo,verbose_name="行政区")
    owner = models.ForeignKey(User,verbose_name="房东")
    type = models.IntegerField(verbose_name="房子类型")
    title = models.TextField(verbose_name="标题")
    introduce = models.TextField(verbose_name="房子介绍")
    facility = models.TextField(verbose_name="房子设施")
    area = models.IntegerField(verbose_name="商圈")
    limit = models.TextField(verbose_name='房客须知')
    auto_reply = models.TextField(verbose_name="自动回复",blank=True)
    price = models.IntegerField(verbose_name="普通价格")
    h_price = models.IntegerField(verbose_name="节假日价格")
    info = models.TextField(verbose_name='房子详情')
    discounts = models.TextField(verbose_name='优惠政策',blank=True)
    book = models.TextField(verbose_name='预订设置')
    photo = models.TextField(verbose_name='照片')
    tag = models.TextField(verbose_name="标签", blank=True)
    location = models.TextField(verbose_name="位置详情")
    flag = models.BooleanField(verbose_name="审核",default=False)

    def __str__(self):
        return str(self.title)

class Order(models.Model):
    order_num = models.CharField(max_length=11,verbose_name="订单号")
    house = models.ForeignKey(HouseInfo, verbose_name="房源")
    customer = models.ForeignKey(User, verbose_name="消费者")
    start_date = models.DateField(verbose_name="订单开始日期")
    end_date = models.DateField(verbose_name="订单结束日期")
    price = models.FloatField(max_length=10, verbose_name="价格")
    liuyan = models.TextField(verbose_name='liuyan',null=True)
    customer_num = models.IntegerField(default=1,verbose_name='入住人数')
    star_num = models.IntegerField(default=5, verbose_name='评星')
    evalute = models.TextField(null=True, verbose_name='评价')

    def __unicode__(self):
        return self.order_num

    def __str__(self):
        return self.order_num

class Order_date(models.Model):
    house = models.ForeignKey(HouseInfo, verbose_name="房源")
    date = models.DateField(verbose_name="订单日期")






