# Generated by Django 5.1.1 on 2024-11-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0031_remove_facturar_biologicosinformacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturar',
            name='cantidad_total',
            field=models.JSONField(default=20),
            preserve_default=False,
        ),
    ]
