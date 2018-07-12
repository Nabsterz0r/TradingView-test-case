# Generated by Django 2.0.2 on 2018-07-11 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClosePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='currentstat',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Symbol'),
        ),
        migrations.AddField(
            model_name='closeprice',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Symbol'),
        ),
    ]
