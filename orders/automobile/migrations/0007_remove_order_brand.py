# Generated by Django 3.2 on 2022-10-12 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0006_auto_20221012_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='brand',
        ),
    ]
