# Generated by Django 2.0.2 on 2018-07-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='symbol',
            name='market',
            field=models.CharField(default='USD', max_length=10),
        ),
        migrations.AddField(
            model_name='symbol',
            name='type',
            field=models.CharField(default='DIGITAL_CURRENCY_DAILY', max_length=100),
        ),
    ]
