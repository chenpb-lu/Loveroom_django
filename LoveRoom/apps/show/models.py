from django.db import models

# Create your models here.
class MetaInconfont(models.Model):
    metaId = models.IntegerField(primary_key=True,verbose_name="标签id")
    value = models.CharField(max_length=50,verbose_name="名称")
    classname = models.CharField(max_length=30,verbose_name="字体类名")
