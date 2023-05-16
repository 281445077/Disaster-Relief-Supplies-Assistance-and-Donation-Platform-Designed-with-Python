from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 


class Qianshou(models.Model):
    paijiid = models.ForeignKey('paiji.Paiji',verbose_name='派寄id' ,default=1, on_delete=models.CASCADE ,db_column='paijiid', editable=False,related_name="qianshou_Paiji_paijiid")  
    shenlingid = models.ForeignKey('shenling.Shenling',verbose_name='申领id' ,default=1, on_delete=models.CASCADE ,db_column='shenlingid', editable=False,related_name="qianshou_Shenling_shenlingid")  
    juanzengid = models.ForeignKey('juanzeng.Juanzeng',verbose_name='捐赠id' ,default=1, on_delete=models.CASCADE ,db_column='juanzengid', editable=False,related_name="qianshou_Juanzeng_juanzengid")  
    bianhao = models.CharField('编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wupin = models.CharField('物品' , max_length = 255,default='') 
    wupinleibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wupinleibie', on_delete=models.CASCADE ,related_name="qianshou_Wupinleibie_wupinleibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    juanzengren = models.CharField('捐赠人' ,db_column='juanzengren' , max_length=50,default='') 
    shenlingrenxingming = models.CharField('申领人姓名' , max_length = 50,default='') 
    shenqingyonghu = models.CharField('申请用户' ,db_column='shenqingyonghu' , max_length=50,default='') 
    qianshoubeizhu = models.TextField('签收备注',default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'qianshou'
        verbose_name = '签收'  #单数形式
        verbose_name_plural = verbose_name #复数形式





