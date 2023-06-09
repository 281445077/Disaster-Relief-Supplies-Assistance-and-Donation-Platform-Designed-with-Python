# Generated by Django 3.2.9 on 2022-04-10 14:43

import common.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wupinleibie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juanzeng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bianhao', models.CharField(default='', max_length=50, verbose_name='编号')),
                ('biaoti', models.CharField(default='', max_length=255, verbose_name='标题')),
                ('wupin', models.CharField(default='', max_length=255, verbose_name='物品')),
                ('tupian', common.models.MyImageField(default='', max_length=255, verbose_name='图片')),
                ('shuliang', models.IntegerField(default=0, verbose_name='数量')),
                ('xiangqingbeizhu', common.models.UMeditorField(default='', verbose_name='详情备注')),
                ('zhuangtai', models.CharField(choices=[('待审核', '待审核'), ('已通过', '已通过'), ('未通过', '未通过'), ('未被领取', '未被领取'), ('已被领取', '已被领取')], default='', max_length=512, verbose_name='状态')),
                ('juanzengren', models.CharField(db_column='juanzengren', default='', max_length=50, verbose_name='捐赠人')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('wupinleibie', models.ForeignKey(db_column='wupinleibie', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='juanzeng_Wupinleibie_wupinleibie', to='wupinleibie.wupinleibie')),
            ],
            options={
                'verbose_name': '捐赠',
                'verbose_name_plural': '捐赠',
                'db_table': 'juanzeng',
            },
        ),
    ]
