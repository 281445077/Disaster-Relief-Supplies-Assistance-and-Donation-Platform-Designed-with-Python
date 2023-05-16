from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.


class Lingqu(models.Model):
    juanzengwuziid = models.ForeignKey('juanzengwuzi.Juanzengwuzi',verbose_name='捐赠物资id' ,default=1, on_delete=models.CASCADE ,db_column='juanzengwuziid', editable=False,related_name="lingqu_Juanzengwuzi_juanzengwuziid")  
    xuqiuxinxiid = models.ForeignKey('xuqiuxinxi.Xuqiuxinxi',verbose_name='需求信息id' ,default=1, on_delete=models.CASCADE ,db_column='xuqiuxinxiid', editable=False,related_name="lingqu_Xuqiuxinxi_xuqiuxinxiid")  
    xuqiubianhao = models.CharField('需求编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    juanzengwuzhi = models.CharField('捐赠物质' , max_length = 255,default='') 
    juanzengshuliang = models.IntegerField('捐赠数量',default=0)  
    juanzengyonghu = models.CharField('捐赠用户' ,db_column='juanzengyonghu' , max_length=50,default='') 
    dengjiren = models.CharField('登记人' ,db_column='dengjiren' , max_length=50,default='') 
    lingqubeizhu = models.TextField('领取备注',default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'lingqu'
        verbose_name = '领取'  #单数形式
        verbose_name_plural = verbose_name #复数形式





