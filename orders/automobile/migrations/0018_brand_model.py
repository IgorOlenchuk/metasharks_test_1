# Generated by Django 3.2 on 2022-10-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0017_auto_20221013_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='model',
            field=models.ManyToManyField(related_name='brand', through='automobile.Order', to='automobile.Model', verbose_name='Марка'),
        ),
    ]
