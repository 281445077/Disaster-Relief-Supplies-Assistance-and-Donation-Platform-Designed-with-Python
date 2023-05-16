from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
LEIXING_CHOICES = (
   ('回收处理' , '回收处理') , 
   ('退还处理' , '退还处理') , 

    )  


class Chuli(models.Model):
    juanjiid = models.ForeignKey('juanji.Juanji',verbose_name='捐寄id' ,default=1, on_delete=models.CASCADE ,db_column='juanjiid', editable=False,related_name="chuli_Juanji_juanjiid")  
    juanzengid = models.ForeignKey('juanzeng.Juanzeng',verbose_name='捐赠id' ,default=1, on_delete=models.CASCADE ,db_column='juanzengid', editable=False,related_name="chuli_Juanzeng_juanzengid")  
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    bianhao = models.CharField('编号' , max_length = 50,default='') 
    wupin = models.CharField('物品' , max_length = 255,default='') 
    wupinleibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wupinleibie', on_delete=models.CASCADE ,related_name="chuli_Wupinleibie_wupinleibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    juanzengren = models.CharField('捐赠人' ,db_column='juanzengren' , max_length=50,default='') 
    leixing = models.CharField('类型' , choices=LEIXING_CHOICES , max_length=512,default='') 
    beizhuxinxi = models.TextField('备注信息',default='') 
    tianjiaren = models.CharField('添加人' ,db_column='tianjiaren' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'chuli'
        verbose_name = '处理'  #单数形式
        verbose_name_plural = verbose_name #复数形式





