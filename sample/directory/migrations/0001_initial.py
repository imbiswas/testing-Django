# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('product_number', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]
