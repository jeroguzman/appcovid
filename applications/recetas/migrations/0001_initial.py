# Generated by Django 3.1.4 on 2021-01-26 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_auto_20210120_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('contenido', models.TextField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.paciente')),
            ],
        ),
    ]
