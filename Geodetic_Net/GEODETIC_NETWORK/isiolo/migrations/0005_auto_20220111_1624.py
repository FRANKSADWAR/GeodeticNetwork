# Generated by Django 2.2.20 on 2022-01-11 13:24

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isiolo', '0004_auto_20220106_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geodetic_Controls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('name', models.CharField(max_length=254)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('e', models.FloatField()),
                ('n', models.FloatField()),
                ('order_field', models.CharField(max_length=254)),
                ('status', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': ' Geodetic Controls Isiolo',
            },
        ),
        migrations.AlterField(
            model_name='controls',
            name='status',
            field=models.CharField(choices=[('Destroyed', 'Destroyed'), ('Missing', 'Missing'), ('Existing', 'Existing'), ('Re-Established', 'Re-Established'), ('New control', 'New control')], max_length=20),
        ),
        migrations.AlterField(
            model_name='reportincidence',
            name='status',
            field=models.CharField(choices=[('Destroyed', 'Destroyed'), ('Missing', 'Missing'), ('Existing', 'Existing'), ('Re-Established', 'Re-Established'), ('New control', 'New control')], max_length=20),
        ),
    ]
