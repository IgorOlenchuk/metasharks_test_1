# Generated by Django 3.2 on 2022-10-13 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0021_auto_20221013_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='brand',
        ),
        migrations.AddField(
            model_name='order',
            name='brand',
            field=models.OneToOneField(default=10.0, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='automobile.brand', verbose_name='Марка'),
            preserve_default=False,
        ),
    ]
