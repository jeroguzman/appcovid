# Generated by Django 3.1.4 on 2021-01-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aMaterno',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='aPaterno',
            field=models.CharField(default=None, max_length=120),
        ),
    ]
