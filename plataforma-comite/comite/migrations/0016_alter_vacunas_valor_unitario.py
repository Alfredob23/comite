# Generated by Django 5.1.1 on 2024-10-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0015_facturar_delete_vacunadores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacunas',
            name='valor_unitario',
            field=models.IntegerField(),
        ),
    ]
