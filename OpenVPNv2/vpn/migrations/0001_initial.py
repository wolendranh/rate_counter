# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certs_user_name', models.TextField()),
            ],
            options={
                'db_table': 'certs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('general_vpn_name', models.TextField()),
                ('general_project_name', models.TextField()),
                ('general_server_ip', models.IPAddressField()),
                ('general_server_port', models.IntegerField()),
            ],
            options={
                'db_table': 'general',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='certs',
            name='certs_general',
            field=models.ForeignKey(to='vpn.General'),
            preserve_default=True,
        ),
    ]
