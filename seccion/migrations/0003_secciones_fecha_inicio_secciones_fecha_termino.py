# Generated by Django 5.1.2 on 2024-12-19 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0002_rename_seccion_secciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='secciones',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='secciones',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
    ]