# Generated by Django 5.1.1 on 2024-10-30 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comite', '0019_alter_facturar_valor_total'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vacunas',
            new_name='Biologicos',
        ),
        migrations.RenameField(
            model_name='facturar',
            old_name='cantidad_vacunas',
            new_name='cantidad_aftosa',
        ),
        migrations.RemoveField(
            model_name='facturar',
            name='vacunas',
        ),
        migrations.AddField(
            model_name='facturar',
            name='biologico_aftosa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facturar_aftosa_set', to='comite.biologicos'),
        ),
        migrations.AddField(
            model_name='facturar',
            name='biologico_cepa19',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facturar_cepa19_set', to='comite.biologicos'),
        ),
        migrations.AddField(
            model_name='facturar',
            name='cantidad_cepa19',
            field=models.IntegerField(default=0),
        ),
    ]
