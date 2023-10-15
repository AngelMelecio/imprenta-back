# Generated by Django 3.1.7 on 2023-10-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Material', '0003_material_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='categoria',
            field=models.CharField(choices=[('Papel', 'Papel'), ('Cartulina', 'Cartulina'), ('Carton', 'Carton'), ('Sobres', 'Sobres'), ('Materia prima', 'Materia prima'), ('Otros', 'Otros')], default='Papel', max_length=20),
        ),
    ]