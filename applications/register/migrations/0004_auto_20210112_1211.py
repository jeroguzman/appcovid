# Generated by Django 3.1.4 on 2021-01-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20210112_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aMaterno',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='user',
            name='aPaterno',
            field=models.CharField(max_length=120),
        ),
    ]