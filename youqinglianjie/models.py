from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.


class Youqinglianjie(models.Model):
    wangzhanmingcheng = models.CharField('网站名称' , max_length = 50,default='') 
    wangzhi = models.CharField('网址' , max_length = 50,default='') 



    class Meta:
        db_table = 'youqinglianjie'
        verbose_name = '友情链接'  #单数形式
        verbose_name_plural = verbose_name #复数形式





