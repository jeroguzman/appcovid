# Generated by Django 3.1.4 on 2021-01-26 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210120_1059'),
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.paciente'),
        ),
    ]