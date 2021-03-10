# Generated by Django 3.0.7 on 2020-07-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_auto_20200628_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='city',
            field=models.CharField(blank=True, max_length=60, verbose_name='Town / City'),
        ),
        migrations.AddField(
            model_name='guest',
            name='county',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='guest',
            name='nation',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='guest',
            name='post_code',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]