# Generated by Django 4.0.4 on 2022-06-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_merge_20220606_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha_creacion',
            field=models.TextField(default='2022-06-06 16:37:36.355564'),
        ),
    ]