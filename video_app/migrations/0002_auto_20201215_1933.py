# Generated by Django 3.1.4 on 2020-12-15 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='person',
            name='role',
        ),
    ]
