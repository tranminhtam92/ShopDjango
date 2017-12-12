# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_user', models.IntegerField()),
                ('id_shop', models.IntegerField()),
                ('time', models.DateTimeField(verbose_name=b'date published')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluate_price', models.IntegerField(default=2, choices=[(1, b'thap'), (2, b'nomal'), (3, b'cao')])),
                ('evaluate_quality', models.IntegerField(default=2, choices=[(1, b'thap'), (2, b'binh thuong'), (3, b'cao')])),
                ('service_attitude', models.IntegerField(default=2, choices=[(1, b'kem'), (2, b'tam duoc'), (3, b'tot')])),
                ('security', models.IntegerField(default=2, choices=[(1, b'kem'), (2, b'tam duoc'), (3, b'tot')])),
                ('id_user', models.IntegerField()),
                ('id_shop', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shop_name', models.CharField(max_length=50)),
                ('desciption', models.TextField()),
                ('address', models.CharField(max_length=60)),
                ('picture', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Subcoment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_comment', models.IntegerField()),
                ('time', models.DateTimeField(verbose_name=b'date published')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
