# Generated by Django 2.1.3 on 2019-02-19 06:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hipodromo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('rif', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=20)),
                ('nombre_dueno', models.CharField(max_length=20)),
                ('fecha_registro', models.DateField(default=django.utils.timezone.now)),
                ('foto', models.ImageField(upload_to='assets/hipodromos/')),
                ('estatus', models.CharField(blank=True, choices=[('a', 'Activo'), ('e', 'Eliminado')], default='a', max_length=1)),
            ],
        ),
    ]
