from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
SHENHEJIEGUO_CHOICES = (
   ('已通过' , '已通过') , 
   ('未通过' , '未通过') , 

    )  


class Xuqiushenhe(models.Model):
    xuqiuxinxiid = models.ForeignKey('xuqiuxinxi.Xuqiuxinxi',verbose_name='需求信息id' ,default=1, on_delete=models.CASCADE ,db_column='xuqiuxinxiid', editable=False,related_name="xuqiushenhe_Xuqiuxinxi_xuqiuxinxiid")  
    xuqiubianhao = models.CharField('需求编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wuzhimingcheng = models.CharField('物质名称' , max_length = 255,default='') 
    wuzhileibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wuzhileibie', on_delete=models.CASCADE ,related_name="xuqiushenhe_Wupinleibie_wuzhileibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    xingming = models.CharField('姓名' , max_length = 50,default='') 
    dengjiren = models.CharField('登记人' ,db_column='dengjiren' , max_length=50,default='') 
    shenhejieguo = models.CharField('审核结果' , choices=SHENHEJIEGUO_CHOICES , max_length=512,default='') 
    shenhebeizhu = models.TextField('审核备注',default='') 
    shenheren = models.CharField('审核人' ,db_column='shenheren' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'xuqiushenhe'
        verbose_name = '需求审核'  #单数形式
        verbose_name_plural = verbose_name #复数形式





