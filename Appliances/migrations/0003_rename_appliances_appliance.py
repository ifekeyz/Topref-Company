# Generated by Django 3.2.7 on 2021-09-23 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appliances', '0002_rename_slider_appliances'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appliances',
            new_name='Appliance',
        ),
    ]
