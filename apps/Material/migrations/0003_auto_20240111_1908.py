# Generated by Django 3.1.7 on 2024-01-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Material', '0002_auto_20231116_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='alturaGuillotina',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='material',
            name='otros',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
