# Generated by Django 3.0.7 on 2020-10-23 12:49

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import marinerbookings.bookings.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('guest_first_name', models.CharField(max_length=255, verbose_name='Guest first name')),
                ('guest_last_name', models.CharField(max_length=255, verbose_name='Guest last name')),
                ('booking_source', models.CharField(choices=[('unspecified', 'Unspecified'), ('airbnb', 'AirBnB'), ('mariners', 'Mariners'), ('friends', 'Friends'), ('owners', 'Owners')], default='unspecified', max_length=20, verbose_name='Booking Source')),
                ('guest_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('guest_mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mobile')),
                ('guest_land_line', models.CharField(blank=True, max_length=20, null=True, verbose_name='Landline')),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=60, verbose_name='Town / City')),
                ('county', models.CharField(blank=True, max_length=30)),
                ('post_code', models.CharField(blank=True, max_length=8)),
                ('nation', models.CharField(blank=True, max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=marinerbookings.bookings.models.get_populate_from, unique=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('partner_first_name', models.CharField(max_length=255, verbose_name='Partner first name')),
                ('partner_last_name', models.CharField(max_length=255, verbose_name='Partner last name')),
                ('child_one', models.CharField(max_length=120, verbose_name='Child one')),
                ('child_two', models.CharField(max_length=120, verbose_name='Child two')),
                ('child_three', models.CharField(max_length=120, verbose_name='Child three')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Guest')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
