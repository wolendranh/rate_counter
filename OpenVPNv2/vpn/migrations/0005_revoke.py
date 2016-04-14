# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0004_auto_20160331_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revoke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certs_revoke_name', models.TextField(max_length=200)),
                ('certs_revoke_status', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'revoke',
            },
            bases=(models.Model,),
        ),
    ]
