from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 


class Xinwenxinxi(models.Model):
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    fenlei = models.ForeignKey('xinwenfenlei.Xinwenfenlei' ,default=1,db_column='fenlei', on_delete=models.CASCADE ,related_name="xinwenxinxi_Xinwenfenlei_fenlei" ) 
    tupian = commonModels.MyImagesField('图片',default='') 
    neirong = commonModels.UMeditorField('内容',default='' ) 
    tianjiaren = models.CharField('添加人' ,db_column='tianjiaren' , max_length=50,default='') 
    dianjilv = models.IntegerField('点击率',default=0)  
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'xinwenxinxi'
        verbose_name = '新闻信息'  #单数形式
        verbose_name_plural = verbose_name #复数形式





