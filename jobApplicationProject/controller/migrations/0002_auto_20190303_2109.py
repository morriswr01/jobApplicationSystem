# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-03 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[(b'Submitted', b'Submitted'), (b'Interview', b'Interview'), (b'Rejected', b'Rejected'), (b'Accepted', b'Accepted')], default=b'Submitted', max_length=10),
        ),
    ]