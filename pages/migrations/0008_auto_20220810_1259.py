# Generated by Django 3.2.5 on 2022-08-10 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_account_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cag_name', models.CharField(max_length=30)),
                ('cag_css', models.CharField(max_length=20)),
                ('cag_img', models.ImageField(upload_to='cag')),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, '生理女'), (1, '生理男')], default=1, null=True),
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=100)),
                ('goods_price', models.IntegerField(default=0)),
                ('goods_desc', models.CharField(max_length=2000)),
                ('goods_img', models.ImageField(upload_to='goods')),
                ('goods_cag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.goodscategory')),
            ],
        ),
    ]