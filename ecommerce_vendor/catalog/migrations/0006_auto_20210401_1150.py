# Generated by Django 3.1.7 on 2021-04-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_total_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_feature',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='today_deal',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand_id',
        ),
        migrations.AddField(
            model_name='product',
            name='brand_id',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.Brand'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.Category'),
        ),
    ]
