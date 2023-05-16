from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
SHENHEJIEGUO_CHOICES = (
   ('已通过' , '已通过') , 
   ('未通过' , '未通过') , 

    )  


class Shenlingshenhe(models.Model):
    shenlingid = models.ForeignKey('shenling.Shenling',verbose_name='申领id' ,default=1, on_delete=models.CASCADE ,db_column='shenlingid', editable=False,related_name="shenlingshenhe_Shenling_shenlingid")  
    juanzengid = models.ForeignKey('juanzeng.Juanzeng',verbose_name='捐赠id' ,default=1, on_delete=models.CASCADE ,db_column='juanzengid', editable=False,related_name="shenlingshenhe_Juanzeng_juanzengid")  
    bianhao = models.CharField('编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wupin = models.CharField('物品' , max_length = 255,default='') 
    wupinleibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wupinleibie', on_delete=models.CASCADE ,related_name="shenlingshenhe_Wupinleibie_wupinleibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    juanzengren = models.CharField('捐赠人' ,db_column='juanzengren' , max_length=50,default='') 
    shenlingrenxingming = models.CharField('申领人姓名' , max_length = 50,default='') 
    shenqingyonghu = models.CharField('申请用户' ,db_column='shenqingyonghu' , max_length=50,default='') 
    shenhejieguo = models.CharField('审核结果' , choices=SHENHEJIEGUO_CHOICES , max_length=512,default='') 
    shenhebeizhu = models.TextField('审核备注',default='') 
    shenheren = models.CharField('审核人' ,db_column='shenheren' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'shenlingshenhe'
        verbose_name = '申领审核'  #单数形式
        verbose_name_plural = verbose_name #复数形式




