# Generated by Django 3.2.9 on 2022-04-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wupinleibie', '0001_initial'),
        ('xuqiuxinxi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xuqiushenhe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuqiubianhao', models.CharField(default='', max_length=50, verbose_name='需求编号')),
                ('biaoti', models.CharField(default='', max_length=255, verbose_name='标题')),
                ('wuzhimingcheng', models.CharField(default='', max_length=255, verbose_name='物质名称')),
                ('shuliang', models.IntegerField(default=0, verbose_name='数量')),
                ('xingming', models.CharField(default='', max_length=50, verbose_name='姓名')),
                ('dengjiren', models.CharField(db_column='dengjiren', default='', max_length=50, verbose_name='登记人')),
                ('shenhejieguo', models.CharField(choices=[('已通过', '已通过'), ('未通过', '未通过')], default='', max_length=512, verbose_name='审核结果')),
                ('shenhebeizhu', models.TextField(default='', verbose_name='审核备注')),
                ('shenheren', models.CharField(db_column='shenheren', default='', max_length=50, verbose_name='审核人')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('wuzhileibie', models.ForeignKey(db_column='wuzhileibie', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='xuqiushenhe_Wupinleibie_wuzhileibie', to='wupinleibie.wupinleibie')),
                ('xuqiuxinxiid', models.ForeignKey(db_column='xuqiuxinxiid', default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='xuqiushenhe_Xuqiuxinxi_xuqiuxinxiid', to='xuqiuxinxi.xuqiuxinxi', verbose_name='需求信息id')),
            ],
            options={
                'verbose_name': '需求审核',
                'verbose_name_plural': '需求审核',
                'db_table': 'xuqiushenhe',
            },
        ),
    ]
