from django.db import models
from apps.house.models import HouseInfo
from apps.Uc.models import User

# Create your models here.
class MetaInconfont(models.Model):
    metaId = models.IntegerField(primary_key=True,verbose_name="标签id")
    value = models.CharField(max_length=50,verbose_name="名称")
    classname = models.CharField(max_length=30,verbose_name="字体类名")

class HouseCollection(models.Model):
    house = models.ForeignKey(HouseInfo,verbose_name="房源",related_name='user_collection_set')
    user = models.ForeignKey(User, verbose_name="收藏者", related_name='user_collection_set')
    create_time = models.DateTimeField("收藏/取消时间", auto_now=True)
    # True表示收藏 ,False表示未收藏
    status = models.BooleanField("收藏状态", default=True)
