# Generated by Django 3.1.7 on 2021-04-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_productmultiimage_productvarientinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvarientinfo',
            name='varientinfo_inventory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productvarientinfo',
            name='varientinfo_price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]