# Generated by Django 3.2 on 2022-10-13 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0011_alter_order_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='brand',
        ),
    ]
