# Generated by Django 3.1.7 on 2023-10-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='gramage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='grosor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]