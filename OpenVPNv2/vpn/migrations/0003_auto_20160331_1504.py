# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0002_auto_20160331_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certs',
            name='certs_general',
            field=models.ForeignKey(default=None, blank=True, to='vpn.General', null=True),
            preserve_default=True,
        ),
    ]
