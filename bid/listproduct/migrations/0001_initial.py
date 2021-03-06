# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-20 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listedproducts',
            fields=[
                ('productid', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=100)),
                ('productdesc', models.CharField(max_length=3000)),
                ('productcategory', models.CharField(max_length=100)),
                ('holdingtimeperiod', models.DateField()),
                ('biddingtimeperiod', models.DateField()),
                ('productprice', models.IntegerField(default=0)),
                ('productImage', models.ImageField(upload_to=b'listedproduct')),
            ],
        ),
    ]
