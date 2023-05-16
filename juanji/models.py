from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
JUANJIZHUANGTAI_CHOICES = (
   ('待审核' , '待审核') , 
   ('已通过' , '已通过') , 
   ('未通过' , '未通过') , 

    )  


class Juanji(models.Model):
    juanzengid = models.ForeignKey('juanzeng.Juanzeng',verbose_name='捐赠id' ,default=1, on_delete=models.CASCADE ,db_column='juanzengid', editable=False,related_name="juanji_Juanzeng_juanzengid")  
    bianhao = models.CharField('编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wupin = models.CharField('物品' , max_length = 255,default='') 
    wupinleibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wupinleibie', on_delete=models.CASCADE ,related_name="juanji_Wupinleibie_wupinleibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    juanzengren = models.CharField('捐赠人' ,db_column='juanzengren' , max_length=50,default='') 
    wuliugongsi = models.CharField('物流公司' , max_length = 50,default='') 
    wuliudanhao = models.CharField('物流单号' , max_length = 50,default='') 
    beizhu = models.TextField('备注',default='') 
    juanjizhuangtai = models.CharField('捐寄状态' , choices=JUANJIZHUANGTAI_CHOICES , max_length=512,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'juanji'
        verbose_name = '捐寄'  #单数形式
        verbose_name_plural = verbose_name #复数形式





