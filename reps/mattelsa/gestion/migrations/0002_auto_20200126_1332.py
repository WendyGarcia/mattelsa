# Generated by Django 3.0.2 on 2020-01-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]
