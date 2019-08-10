from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    realname = models.CharField(max_length=8, verbose_name="真实姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    qq = models.CharField(max_length=11, verbose_name="QQ号")
    wechat = models.CharField(max_length=15,verbose_name="微信号")
    weibo = models.CharField(max_length=15,verbose_name="微博号")
    avator_sor = models.ImageField(upload_to="avator/", default="avator/default.jpg", verbose_name="头像")
    ID_num = models.CharField(max_length=18,verbose_name="身份证号")
    # 0表示男，1表示女，2表示保密
    SEX_CHOICES = (
        (0, '男'),
        (1, '女'),
        (None, '保密'),  # 把------去掉
    )
    sex = models.IntegerField(choices=SEX_CHOICES, null=True, blank=True, default=None, verbose_name="性别")
    introduce = models.TextField(verbose_name="自我介绍")
    nickname = models.CharField(max_length=24, verbose_name="昵称")

    def __str__(self):
        return self.nickname


