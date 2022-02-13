# Generated by Django 2.2.20 on 2021-11-21 11:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('county3_field', models.FloatField()),
                ('county3_id', models.FloatField()),
                ('county', models.CharField(max_length=20)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Isiolo',
            },
        ),
        migrations.CreateModel(
            name='Towns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('town_name', models.CharField(max_length=254)),
                ('town_id', models.FloatField()),
                ('town_type', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Towns',
            },
        ),
    ]
