# Generated by Django 3.0.2 on 2020-01-26 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20200126_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.Cliente', verbose_name='cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='celda',
            name='numero',
            field=models.IntegerField(verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='puertas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Puertas'),
        ),
    ]
