# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('approved_transfer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvedtransfer',
            name='status',
            field=models.CharField(default=b'transfer', max_length=20),
        ),
    ]
