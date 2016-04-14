# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0005_revoke'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropDwon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('codition', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'drop',
            },
            bases=(models.Model,),
        ),
    ]
