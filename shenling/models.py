from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
SHENLINGRENXINGBIE_CHOICES = (
   ('男' , '男') , 
   ('女' , '女') , 

    )  
SHENLINGZHUANGTAI_CHOICES = (
   ('待审核' , '待审核') , 
   ('已通过' , '已通过') , 
   ('未通过' , '未通过') , 

    )  


class Shenling(models.Model):
    juanzengid = models.ForeignKey('juanzeng.Juanzeng',verbose_name='捐赠id' ,default=1, on_delete=models.CASCADE ,db_column='juanzengid', editable=False,related_name="shenling_Juanzeng_juanzengid")  
    bianhao = models.CharField('编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wupin = models.CharField('物品' , max_length = 255,default='') 
    wupinleibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wupinleibie', on_delete=models.CASCADE ,related_name="shenling_Wupinleibie_wupinleibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    juanzengren = models.CharField('捐赠人' ,db_column='juanzengren' , max_length=50,default='') 
    shenlingrenxingming = models.CharField('申领人姓名' , max_length = 50,default='') 
    shenlingrenxingbie = models.CharField('申领人性别' , choices=SHENLINGRENXINGBIE_CHOICES , max_length=512,default='') 
    shenlingrendianhua = models.CharField('申领人电话' , max_length = 50,default='') 
    shenlingrendizhi = models.CharField('申领人地址' , max_length = 50,default='') 
    shenqingmiaoshu = models.TextField('申请描述',default='') 
    shenlingzhuangtai = models.CharField('申领状态' , choices=SHENLINGZHUANGTAI_CHOICES , max_length=512,default='') 
    shenqingyonghu = models.CharField('申请用户' ,db_column='shenqingyonghu' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'shenling'
        verbose_name = '申领'  #单数形式
        verbose_name_plural = verbose_name #复数形式





