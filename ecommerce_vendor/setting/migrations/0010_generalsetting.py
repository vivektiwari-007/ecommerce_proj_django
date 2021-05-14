# Generated by Django 3.1.7 on 2021-04-07 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0009_auto_20210407_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('generalsetting_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('store_address', models.CharField(blank=True, max_length=100, null=True)),
                ('maintenance', models.BooleanField(blank=True, null=True)),
                ('store_logo', models.ImageField(blank=True, null=True, upload_to='general_store_logo/')),
                ('store_email_logo', models.ImageField(blank=True, null=True, upload_to='general_store_email_logo/')),
                ('store_invoice_logo', models.ImageField(blank=True, null=True, upload_to='general_store_invoice_logo/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.country')),
                ('currency_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.currency')),
                ('language_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.language')),
                ('zone_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.zone')),
            ],
        ),
    ]
