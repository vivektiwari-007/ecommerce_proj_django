# Generated by Django 3.1.7 on 2021-04-07 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0008_auto_20210407_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='created_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='modified_by',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='modified_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tax',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]