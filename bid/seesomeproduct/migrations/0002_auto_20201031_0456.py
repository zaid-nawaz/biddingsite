# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-31 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seesomeproduct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biddingprice',
            name='Bid_on_productid',
            field=models.CharField(max_length=10),
        ),
    ]
