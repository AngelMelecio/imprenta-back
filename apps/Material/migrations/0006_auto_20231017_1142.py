# Generated by Django 3.1.7 on 2023-10-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Material', '0005_auto_20231015_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='gramaje',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]