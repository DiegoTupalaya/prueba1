# Generated by Django 3.1.4 on 2021-01-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]