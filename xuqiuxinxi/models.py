from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
ZHUANGTAI_CHOICES = (
   ('待审核' , '待审核') , 
   ('未通过' , '未通过') , 
   ('待捐赠' , '待捐赠') , 
   ('已领取' , '已领取') , 

    )  


class Xuqiuxinxi(models.Model):
    xuqiubianhao = models.CharField('需求编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wuzhimingcheng = models.CharField('物质名称' , max_length = 255,default='') 
    wuzhileibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wuzhileibie', on_delete=models.CASCADE ,related_name="xuqiuxinxi_Wupinleibie_wuzhileibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    xingming = models.CharField('姓名' , max_length = 50,default='') 
    shoujihao = models.CharField('手机号' , max_length = 50,default='') 
    lianxidizhi = models.CharField('联系地址' , max_length = 50,default='') 
    xuqiumiaoshu = models.TextField('需求描述',default='') 
    zhuangtai = models.CharField('状态' , choices=ZHUANGTAI_CHOICES , max_length=512,default='') 
    dengjiren = models.CharField('登记人' ,db_column='dengjiren' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'xuqiuxinxi'
        verbose_name = '需求信息'  #单数形式
        verbose_name_plural = verbose_name #复数形式





