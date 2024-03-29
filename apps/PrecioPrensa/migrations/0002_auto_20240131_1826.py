# Generated by Django 3.1.7 on 2024-02-01 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prensa', '0001_initial'),
        ('TipoImpresion', '0001_initial'),
        ('PrecioPrensa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='precioprensa',
            old_name='precioCantidad',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='precioprensa',
            name='precioColor',
        ),
        migrations.RemoveField(
            model_name='precioprensa',
            name='tinta',
        ),
        migrations.AlterField(
            model_name='precioprensa',
            name='prensa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Prensa.prensa'),
        ),
        migrations.AlterField(
            model_name='precioprensa',
            name='tipoImpresion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TipoImpresion.tipoimpresion'),
        ),
    ]
