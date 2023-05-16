from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
ZHUANGTAI_CHOICES = (
   ('待审核' , '待审核') , 
   ('已通过' , '已通过') , 
   ('未通过' , '未通过') , 
   ('未被领取' , '未被领取') , 
   ('已被领取' , '已被领取') , 

    )  


class Juanzeng(models.Model):
    bianhao = models.CharField('编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wupin = models.CharField('物品' , max_length = 255,default='') 
    wupinleibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wupinleibie', on_delete=models.CASCADE ,related_name="juanzeng_Wupinleibie_wupinleibie" ) 
    tupian = commonModels.MyImagesField('图片',default='') 
    shuliang = models.IntegerField('数量',default=0)  
    xiangqingbeizhu = commonModels.UMeditorField('详情备注',default='' ) 
    zhuangtai = models.CharField('状态' , choices=ZHUANGTAI_CHOICES , max_length=512,default='') 
    juanzengren = models.CharField('捐赠人' ,db_column='juanzengren' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'juanzeng'
        verbose_name = '捐赠'  #单数形式
        verbose_name_plural = verbose_name #复数形式





