# Generated by Django 2.1.3 on 2019-02-19 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20190219_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_u',
            field=models.ForeignKey(blank=True, default='user', null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Type_User'),
        ),
    ]
