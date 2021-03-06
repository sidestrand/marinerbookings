# Generated by Django 3.1.1 on 2021-03-09 17:20

import autoslug.fields
from django.db import migrations
import marinerbookings.bookings.models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20210309_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=marinerbookings.bookings.models.get_populate_from, unique=True),
        ),
    ]
