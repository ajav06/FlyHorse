# Generated by Django 2.1.3 on 2019-02-19 06:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hipodromo', '0001_initial'),
        ('entrenador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caballo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('peso', models.FloatField(max_length=4, null=True)),
                ('fecha_Registro', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('fecha_nac', models.DateField(default=django.utils.timezone.now)),
                ('foto', models.ImageField(upload_to='assets/caballos/')),
                ('estatus', models.CharField(blank=True, choices=[('a', 'Activo'), ('e', 'Eliminado')], default='a', max_length=1)),
                ('id_entre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrenador.Entrenador')),
                ('id_hip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hipodromo.Hipodromo')),
            ],
        ),
    ]
