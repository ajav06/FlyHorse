# Generated by Django 2.1.3 on 2019-02-19 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_u',
            field=models.ForeignKey(blank=True, default='admin', null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Type_User'),
        ),
    ]
