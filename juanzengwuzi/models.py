from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
 
JUANZENGZHUANGTAI_CHOICES = (
   ('待领取' , '待领取') , 
   ('已领取' , '已领取') , 

    )  


class Juanzengwuzi(models.Model):
    xuqiuxinxiid = models.ForeignKey('xuqiuxinxi.Xuqiuxinxi',verbose_name='需求信息id' ,default=1, on_delete=models.CASCADE ,db_column='xuqiuxinxiid', editable=False,related_name="juanzengwuzi_Xuqiuxinxi_xuqiuxinxiid")  
    xuqiubianhao = models.CharField('需求编号' , max_length = 50,default='') 
    biaoti = models.CharField('标题' , max_length = 255,default='') 
    wuzhimingcheng = models.CharField('物质名称' , max_length = 255,default='') 
    wuzhileibie = models.ForeignKey('wupinleibie.Wupinleibie' ,default=1,db_column='wuzhileibie', on_delete=models.CASCADE ,related_name="juanzengwuzi_Wupinleibie_wuzhileibie" ) 
    shuliang = models.IntegerField('数量',default=0)  
    xingming = models.CharField('姓名' , max_length = 50,default='') 
    shoujihao = models.CharField('手机号' , max_length = 50,default='') 
    lianxidizhi = models.CharField('联系地址' , max_length = 50,default='') 
    dengjiren = models.CharField('登记人' ,db_column='dengjiren' , max_length=50,default='') 
    juanzengwuzhi = models.CharField('捐赠物质' , max_length = 255,default='') 
    juanzengshuliang = models.IntegerField('捐赠数量',default=0)  
    kuaidigongsi = models.CharField('快递公司' , max_length = 50,default='') 
    kuaididanhao = models.CharField('快递单号' , max_length = 50,default='') 
    juanzengbeizhu = models.TextField('捐赠备注',default='') 
    juanzengrennicheng = models.CharField('捐赠人昵称' , max_length = 50,default='') 
    juanzengzhuangtai = models.CharField('捐赠状态' , choices=JUANZENGZHUANGTAI_CHOICES , max_length=512,default='') 
    juanzengyonghu = models.CharField('捐赠用户' ,db_column='juanzengyonghu' , max_length=50,default='') 
    addtime = models.DateTimeField('添加时间' , auto_now_add=True) 



    class Meta:
        db_table = 'juanzengwuzi'
        verbose_name = '捐赠物资'  #单数形式
        verbose_name_plural = verbose_name #复数形式





