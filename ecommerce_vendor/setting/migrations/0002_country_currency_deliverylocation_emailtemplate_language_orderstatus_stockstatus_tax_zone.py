# Generated by Django 3.1.7 on 2021-04-05 10:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('iso_code_1', models.CharField(blank=True, max_length=100, null=True)),
                ('iso_code_2', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code_required', models.BooleanField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol_left', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol_right', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryLocation',
            fields=[
                ('deliverylocation_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_location', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('emailtemplate_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='language/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('orderstatus_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('select_color', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='StockStatus',
            fields=[
                ('stockstatus_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('tax_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('zone_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('modified_date', models.DateField(default=datetime.date.today)),
                ('Country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.country')),
            ],
        ),
    ]