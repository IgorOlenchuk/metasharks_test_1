# Generated by Django 3.2 on 2022-10-12 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0005_order_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
        migrations.AlterField(
            model_name='order',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='automobile.brand'),
        ),
    ]
