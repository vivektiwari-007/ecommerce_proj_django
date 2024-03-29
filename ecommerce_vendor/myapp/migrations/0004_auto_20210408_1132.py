# Generated by Django 3.1.7 on 2021-04-08 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0010_generalsetting'),
        ('myapp', '0003_auto_20210324_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
