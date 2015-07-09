# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.URLField(max_length=255, verbose_name='Topic')),
                ('hub', models.URLField(max_length=255, verbose_name='Hub')),
                ('verify_token', models.CharField(max_length=255, null=True, verbose_name='Verify Token', blank=True)),
                ('lease_expiration', models.DateTimeField(verbose_name='Lease expiration', null=True, editable=False, blank=True)),
                ('secret', models.CharField(max_length=255, null=True, verbose_name='Secret', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=0, editable=False, choices=[(0, 'inactive'), (1, 'active'), (2, 'verifying'), (3, 'subscribe action rejected'), (4, 'unsubscribe action rejected')])),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('topic', 'site')]),
        ),
    ]
