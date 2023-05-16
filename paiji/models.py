from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
SHENLINGRENXINGBIE_CHOICES = (
   ('男' , '男') , 
   ('女' , '女') , 

    )  


class Paiji(models.Model):
    shenlingid = models.ForeignKey('shenling.Shenling',verbose_name='申领id' ,default=1, on_delete=models.CASCADE ,db_column='shenlingid', editable=False,related_name="paiji_Shenling_shenlingid")  
    juanzengid = models.ForeignKey('juanzeng.Juanzeng',verbose_name='捐赠id' ,default=1, on_delete=models.CASCADE ,db_column='juanzengid', editable=False,related_name="paiji_Juanzeng_juanzengid")  
    bianhao = models.CharField('编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wupin = models.CharField('物品' , max_length = 255,default='') 
    wupinleibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wupinleibie', on_delete=models.CASCADE ,related_name="paiji_Wupinleibie_wupinleibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    juanzengren = models.CharField('捐赠人' ,db_column='juanzengren' , max_length=50,default='') 
    shenlingrenxingming = models.CharField('申领人姓名' , max_length = 50,default='') 
    shenlingrenxingbie = models.CharField('申领人性别' , choices=SHENLINGRENXINGBIE_CHOICES , max_length=512,default='') 
    shenlingrendianhua = models.CharField('申领人电话' , max_length = 50,default='') 
    shenlingrendizhi = models.CharField('申领人地址' , max_length = 50,default='') 
    shenqingyonghu = models.CharField('申请用户' ,db_column='shenqingyonghu' , max_length=50,default='') 
    wuliugongsi = models.CharField('物流公司' , max_length = 50,default='') 
    wuliudanhao = models.CharField('物流单号' , max_length = 50,default='') 
    beizhu = models.TextField('备注',default='') 
    caozuoren = models.CharField('操作人' ,db_column='caozuoren' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'paiji'
        verbose_name = '派寄'  #单数形式
        verbose_name_plural = verbose_name #复数形式





