# Generated by Django 4.0.6 on 2022-08-16 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setslistingpage',
            name='set_id',
        ),
        migrations.RemoveField(
            model_name='setslistingpage',
            name='set_name',
        ),
    ]
