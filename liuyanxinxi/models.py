from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.


class Liuyanxinxi(models.Model):
    shouxinren = models.CharField('收信人' ,db_column='shouxinren' , max_length=50,default='') 
    xinxineirong = models.TextField('信息内容',default='') 
    faxinren = models.CharField('发信人' ,db_column='faxinren' , max_length=50,default='') 
    huifuneirong = models.TextField('回复内容',default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'liuyanxinxi'
        verbose_name = '留言信息'  #单数形式
        verbose_name_plural = verbose_name #复数形式





