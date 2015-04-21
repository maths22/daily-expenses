# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateTimeField(verbose_name='date spent')),
            ],
        ),
    ]
