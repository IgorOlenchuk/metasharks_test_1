# Generated by Django 3.2 on 2022-10-12 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0008_order_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='automobile.brand', verbose_name='Марка'),
        ),
    ]
