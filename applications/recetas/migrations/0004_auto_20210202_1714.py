# Generated by Django 3.1.5 on 2021-02-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_auto_20210202_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='static/img/recetas/qr'),
        ),
    ]
