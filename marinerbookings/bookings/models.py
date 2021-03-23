from django.db import models
from django.urls import reverse
from django import forms
from django.conf import settings

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from localflavor.gb.forms import GBCountySelect, GBNationSelect, GBPostcodeField

    
import datetime

tdy = datetime.date.today()	
td = tdy.isoformat()

def get_populate_from(instance):
    return '%s-%s' % (instance.guest_first_name, instance.guest_last_name)

class Guest(models.Model):
    
    # class BookingSource(models.TextChoices):
        # UNSPECIFIED = "unspecified", "Unspecified"
        # AIRBNB = "airbnb", "AirBnB"
        # MARINERS = "mariners", "Mariners"
        # FRIENDS = "friends", "Friends"
        # OWNERS = "owners", "Owners" 
        
    guest_first_name = models.CharField("Guest first name", max_length=255)
    guest_last_name = models.CharField("Guest last name", max_length=255)
    # booking_source = models.CharField("Booking Source", max_length=20,      
        # choices=BookingSource.choices, default=BookingSource.UNSPECIFIED)
    guest_email = models.EmailField('email', blank=True, null=True)
    guest_mobile = models.CharField('Mobile', max_length=20, blank=True, null=True)
    guest_land_line = models.CharField('Landline', max_length=20, blank=True, null=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=60, blank=True, verbose_name='Town / City')
    county = models.CharField(max_length=30, blank=True)
    post_code = models.CharField(max_length=8, blank=True)
    nation = models.CharField(max_length=20, blank=True)
    num_child = models.IntegerField(default=0)
    slug = AutoSlugField(unique=True, populate_from=get_populate_from)
    
    @property
    def guest_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.guest_first_name, self.guest_last_name)
            
    def __str__(self):
        return self.guest_full_name
        
    def get_absolute_url(self):
        """Return absolute URL to the Guest Detail page."""
        return reverse(
            'guest_detail', kwargs={"slug": self.slug}
        )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    
class Family(TimeStampedModel):
    guest = models.ForeignKey(
        'Guest',
        on_delete=models.DO_NOTHING,
        )
    partner_first_name = models.CharField("Partner first name", max_length=255)
    partner_last_name = models.CharField("Partner last name", max_length=255)
    child_one = models.CharField("Child one", max_length=120)
    child_two = models.CharField("Child two", max_length=120)
    child_three = models.CharField("Child three", max_length=120)


def get_populate_from(self):
    dt = self.start_date.toordinal()
    return '%s' % (dt)
    
class BookingPeriods(models.Manager):   
    def get_queryset(self):
        return super().get_queryset().filter(start_date__gte=tdy)
    
class BookingDepositDue(models.Manager):   
    def get_queryset(self):
        return super().get_queryset().filter(ack_date__lt = tdy
        ).exclude(dep_recd__isnull=False
        )
    
class BookingBalanceDue(models.Manager):   
    def get_queryset(self):
        return super().get_queryset().filter(bal_recd__isnull=True)
    
class BookingSecurityDepRecd(models.Manager):   
    def get_queryset(self):
        return super().get_queryset().filter(sec_recd__lt=1)
    
class BookingKeysSent(models.Manager):   
    def get_queryset(self):
        return super().get_queryset().filter(keys_sent__isnull=True)
    
class BookingSecReturned(models.Manager):   
    def get_queryset(self):
        return super().get_queryset().filter(sec_retn__isnull=True)
    
class Booking(models.Model):
    
    class BookingStatus(models.IntegerChoices):
        ENQUIRY = 0
        ACKNOWLEDGED = 1
        DEPOSIT_RECEIVED = 2
        BALANCE_RECEIVED = 3
        KEYS_SENT = 4
        STAY_COMPLETE = 5

    class GuestStatus(models.IntegerChoices):
        GUEST = 0
        FRIEND = 1
        OWNERS = 2
        AIRBNB = 3

    class SecurityStatus(models.IntegerChoices):
        UNPAID = 0
        SEPARATE_CHEQUE = 1
        PAYM = 2
        BACS = 3
        NOT_REQUIRED = 4

    guest = models.ForeignKey(
        'Guest',
        on_delete=models.DO_NOTHING,
        )
    guest_status = models.IntegerField('Guest status', choices=GuestStatus.choices, default=0)
    ack_date = models.DateField(verbose_name='Date acknowledged')
    start_date = models.DateField(verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    dep_recd = models.DateField(null=True, blank=True, verbose_name='Deposit received')
    bal_amount = models.IntegerField('Balance due', default=0)
    dep_amount = models.IntegerField('Deposit amount', default=0)
    sec_recd = models.IntegerField('Security deposit', choices=SecurityStatus.choices, default=0)
    bal_recd = models.DateField(null=True, blank=True, verbose_name='Balance received')
    keys_sent = models.DateField(null=True, blank=True, verbose_name='Date keys sent')
    sec_retn = models.DateField(null=True, blank=True, verbose_name='Security deposit returned')
    booking_status = models.IntegerField('Status', choices=BookingStatus.choices, default=3)
    booking_notes = models.TextField(blank=True, verbose_name='Notes')
    bkd_child = models.IntegerField('Children', default=0)
    bkd_adult = models.IntegerField('Adults', default=2)
    guest_one = models.CharField(blank=True, verbose_name='Guest 1', max_length=30)
    guest_two = models.CharField(blank=True, verbose_name='Guest 2', max_length=30)
    guest_three = models.CharField(blank=True, verbose_name='Guest 3', max_length=30)
    guest_three = models.CharField(blank=True, verbose_name='Guest 3', max_length=30)
    slug = AutoSlugField(unique=True, populate_from=get_populate_from)
    num_nights = models.IntegerField('Nights', default=0)
    objects = models.Manager()
    future_bookings = BookingPeriods()
    booking_balance = BookingBalanceDue()
    booking_deposit = BookingDepositDue()
    booking_sec_recd = BookingSecurityDepRecd()
    booking_keys_sent = BookingKeysSent()
    booking_sec_returned = BookingSecReturned()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    
    @property
    def have_returned_sec(self):
        if self.booking_status == 4 and not self.sec_retn:
            return True
        else:
            return False
        
    def num_nights(self):
        sd = (self.start_date.toordinal())
        ed = (self.end_date.toordinal())
        num_nights = (ed - sd)
        return '%s' % (num_nights)

    def bal_due(self):
        bal_due = (self.start_date - datetime.timedelta(weeks=6))
        if not self.bal_recd and self.bkg_source == 0 and (datetime.date.today() >= self.start_date - datetime.timedelta(weeks=6)):
            return '%s' % (bal_due)
        
    def sec_due(self):
        sec_due = (self.start_date - datetime.timedelta(weeks = 2))
        if datetime.date.today() >= sec_due and not self.sec_recd and self.bkg_source == 0:
            return '%s' % (sec_due)
        
    def send_keys(self):
        send_keys = (self.start_date - datetime.timedelta(weeks = 2))
        if datetime.date.today() >= send_keys and not self.keys_sent and self.bkg_source != 2:
            return '%s' % (send_keys)
        
    def return_sec(self):
        return_sec = (self.end_date)
        if self.bkg_source == 0 and self.end_date <= datetime.date.today() and self.booking_status <5:
            return '%s' % (return_sec)
        elif self.booking_status == 4 and self.sec_retn:
            self.booking_status = 5
        super(Booking, self).save()
            
    # def future_bookings(self):  # returns guests with a current or future booking
        # future_bookings = (self.guest)
        # if self.end_date >= datetime.date.today():
            # return '%s - %s  %s' % (self.start_date, self.end_date, self.guest)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
         
    @property
    def booking_details(self):
        "Returns the guest name and booking dates."
        return '%s:  %s - %s' % (self.guest, self.start_date, self.ack_date)
            
    def __str__(self):
        return self.booking_details
        
    def get_absolute_url(self):
        """Return absolute URL to the Bookings Detail page."""
        return reverse(
            'detail', kwargs={"slug": self.slug}
        )         
    
