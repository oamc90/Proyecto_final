# Generated by Django 4.0.4 on 2022-06-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_alter_mensaje_contenido_alter_mensaje_fecha_envio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha_envio',
            field=models.TextField(default='2022-06-06 07:44:41.303662'),
        ),
    ]
