from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.


class Lunbotu(models.Model):
    title = models.CharField('标题' , max_length = 50,default='') 
    image = commonModels.MyImageField('图片',default='') 
    url = models.CharField('连接地址' , max_length = 255,default='') 



    class Meta:
        db_table = 'lunbotu'
        verbose_name = '轮播图'  #单数形式
        verbose_name_plural = verbose_name #复数形式





