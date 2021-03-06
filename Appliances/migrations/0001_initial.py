# Generated by Django 3.2.7 on 2021-09-23 03:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('price', models.CharField(blank=True, max_length=20)),
                ('brief', models.TextField(default=True)),
                ('maker', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('gradeType', models.CharField(max_length=20)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
