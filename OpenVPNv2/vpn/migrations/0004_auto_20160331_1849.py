# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0003_auto_20160331_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certs',
            name='certs_general',
            field=models.ForeignKey(default=1, to='vpn.General'),
            preserve_default=False,
        ),
    ]
