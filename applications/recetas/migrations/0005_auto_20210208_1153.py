# Generated by Django 3.1.5 on 2021-02-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_auto_20210202_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/recetas/qr'),
        ),
    ]