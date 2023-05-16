from django.db import models
from common import models as commonModels
from django.contrib.auth import models as authModels

# Create your models here.
XINGBIE_CHOICES = (
   ('男' , '男') , 
   ('女' , '女') , 

    )  


class Yonghu(models.Model):
    yonghuming = models.CharField('用户名' , max_length = 50,default='') 
    mima = models.CharField('密码' , max_length = 128,default='') 
    xingming = models.CharField('姓名' , max_length = 50,default='') 
    nicheng = models.CharField('昵称' , max_length = 50,default='') 
    xingbie = models.CharField('性别' , choices=XINGBIE_CHOICES , max_length=512,default='') 
    shoujihao = models.CharField('手机号' , max_length = 50,default='') 
    youxiang = models.CharField('邮箱' , max_length = 50,default='') 
    shenfenzheng = models.CharField('身份证' , max_length = 50,default='') 
    dizhi = models.CharField('地址' , max_length = 50,default='') 
    aixinjifen = models.DecimalField('爱心积分' ,default=0,max_digits=16,decimal_places=2) 



    class Meta:
        db_table = 'yonghu'
        verbose_name = '用户'  #单数形式
        verbose_name_plural = verbose_name #复数形式





