# Generated by Django 3.2.7 on 2021-09-23 03:34

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
                ('tag', models.CharField(blank=True, max_length=20)),
                ('image1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('is_needed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('message', models.TextField(blank=True)),
                ('is_needed', models.BooleanField(default=True)),
            ],
        ),
    ]
