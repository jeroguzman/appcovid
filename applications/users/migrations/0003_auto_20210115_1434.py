# Generated by Django 3.1.4 on 2021-01-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210115_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
    ]