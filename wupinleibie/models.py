from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.


class Wupinleibie(models.Model):
    leibieming = models.CharField('类别名' , max_length = 50,default='') 



    class Meta:
        db_table = 'wupinleibie'
        verbose_name = '物品类别'  #单数形式
        verbose_name_plural = verbose_name #复数形式





