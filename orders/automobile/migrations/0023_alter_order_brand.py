# Generated by Django 3.2 on 2022-10-13 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0022_auto_20221013_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='automobile.brand', verbose_name='Марка'),
        ),
    ]
