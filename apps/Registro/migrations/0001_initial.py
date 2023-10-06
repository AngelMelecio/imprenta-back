# Generated by Django 3.1.7 on 2023-09-21 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('idRegistro', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(max_length=200)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
