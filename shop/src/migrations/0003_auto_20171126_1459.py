# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20171122_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='desciption',
            new_name='description',
        ),
    ]
