# Generated by Django 3.2.9 on 2022-04-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('juanzengwuzi', '0001_initial'),
        ('xuqiuxinxi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lingqu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuqiubianhao', models.CharField(default='', max_length=50, verbose_name='需求编号')),
                ('biaoti', models.CharField(default='', max_length=255, verbose_name='标题')),
                ('juanzengwuzhi', models.CharField(default='', max_length=255, verbose_name='捐赠物质')),
                ('juanzengshuliang', models.IntegerField(default=0, verbose_name='捐赠数量')),
                ('juanzengyonghu', models.CharField(db_column='juanzengyonghu', default='', max_length=50, verbose_name='捐赠用户')),
                ('dengjiren', models.CharField(db_column='dengjiren', default='', max_length=50, verbose_name='登记人')),
                ('lingqubeizhu', models.TextField(default='', verbose_name='领取备注')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('juanzengwuziid', models.ForeignKey(db_column='juanzengwuziid', default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='lingqu_Juanzengwuzi_juanzengwuziid', to='juanzengwuzi.juanzengwuzi', verbose_name='捐赠物资id')),
                ('xuqiuxinxiid', models.ForeignKey(db_column='xuqiuxinxiid', default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='lingqu_Xuqiuxinxi_xuqiuxinxiid', to='xuqiuxinxi.xuqiuxinxi', verbose_name='需求信息id')),
            ],
            options={
                'verbose_name': '领取',
                'verbose_name_plural': '领取',
                'db_table': 'lingqu',
            },
        ),
    ]
