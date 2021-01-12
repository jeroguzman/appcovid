# Generated by Django 3.1.4 on 2021-01-12 19:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20210112_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avisoPrivacidad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='contrasena',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contrasena2',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='correo',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cp',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.RegexValidator('^\\d{5}$')]),
        ),
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='edad',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='user',
            name='sexo',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
