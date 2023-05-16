from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.


class Xinwenfenlei(models.Model):
    fenleimingcheng = models.CharField('分类名称' , max_length = 50,default='') 



    class Meta:
        db_table = 'xinwenfenlei'
        verbose_name = '新闻分类'  #单数形式
        verbose_name_plural = verbose_name #复数形式





