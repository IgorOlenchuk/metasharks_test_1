# Generated by Django 3.2 on 2022-10-12 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='brand',
            field=models.ForeignKey(default=10.0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='brands', to='automobile.brand', verbose_name='Марка'),
            preserve_default=False,
        ),
    ]
