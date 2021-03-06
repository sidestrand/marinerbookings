# Generated by Django 3.1.1 on 2021-03-09 17:15

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import marinerbookings.bookings.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookings.guest'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=marinerbookings.bookings.models.get_populate_from, unique=True),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_status', models.IntegerField(choices=[(0, 'Guest'), (1, 'Friend'), (2, 'Owners'), (3, 'Airbnb')], default=0, verbose_name='Guest status')),
                ('ack_date', models.DateField(verbose_name='Date acknowledged')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('dep_recd', models.DateField(blank=True, null=True, verbose_name='Deposit received')),
                ('bal_amount', models.IntegerField(default=0, verbose_name='Balance due')),
                ('dep_amount', models.IntegerField(default=0, verbose_name='Deposit amount')),
                ('sec_recd', models.IntegerField(choices=[(0, 'Unpaid'), (1, 'Separate Cheque'), (2, 'Paym'), (3, 'Bacs'), (4, 'Not Required')], default=0, verbose_name='Security deposit')),
                ('bal_recd', models.DateField(blank=True, null=True, verbose_name='Balance received')),
                ('keys_sent', models.DateField(blank=True, null=True, verbose_name='Date keys sent')),
                ('sec_retn', models.DateField(blank=True, null=True, verbose_name='Security deposit returned')),
                ('booking_status', models.IntegerField(choices=[(0, 'Enquiry'), (1, 'Acknowledged'), (2, 'Deposit Received'), (3, 'Balance Received'), (4, 'Keys Sent'), (5, 'Stay Complete')], default=0, verbose_name='Status')),
                ('booking_notes', models.TextField(blank=True, verbose_name='Notes')),
                ('bkd_child', models.IntegerField(default=0, verbose_name='Children')),
                ('bkd_adult', models.IntegerField(default=2, verbose_name='Adults')),
                ('guest_one', models.CharField(blank=True, max_length=30, verbose_name='Guest 1')),
                ('guest_two', models.CharField(blank=True, max_length=30, verbose_name='Guest 2')),
                ('guest_three', models.CharField(blank=True, max_length=30, verbose_name='Guest 3')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=marinerbookings.bookings.models.get_populate_from, unique=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bookings.guest')),
            ],
        ),
    ]
