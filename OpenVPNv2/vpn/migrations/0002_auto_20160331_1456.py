# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certs',
            name='certs_user_name',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='general',
            name='general_project_name',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='general',
            name='general_vpn_name',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]
