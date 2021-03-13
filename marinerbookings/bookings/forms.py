from django import forms
from .models import Booking, Guest

from localflavor.gb.forms import GBPostcodeField, GBCountySelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import FormActions, AppendedText, PrependedText

class GuestCreateForm(forms.ModelForm):
    
    class Meta:
        model = Guest
        fields = [
            'guest_first_name', 
            'guest_last_name',
            'guest_email',
            'guest_mobile',
            'guest_land_line',
            # 'booking_source'
         ]
     
class GuestUpdateForm(GuestCreateForm):
    
    post_code = GBPostcodeField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['guest_mobile']
        # self.fields['guest_land_line']
        self.fields['address']
        self.fields['city']
        self.fields['county']
        self.fields['post_code']
        
    class Meta(GuestCreateForm.Meta):
        widgets = { 'county': GBCountySelect()}
        # show all the fields!
        fields = [
            'guest_first_name',
            'guest_last_name',
            # 'booking_source	',
            'guest_email',
            'guest_mobile',
            'guest_land_line',
            'address',
            'city',
            'county',
            'post_code',
            'nation',
        ]     

class BookingCreateForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = [
            'guest',
            'guest_status',
            'ack_date',
            'start_date',
            'end_date',
            ]
     
class BookingUpdateForm(BookingCreateForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guest_one']
        self.fields['guest_two']
        self.fields['guest_three']
        self.fields['dep_recd']
        self.fields['dep_amount']
        self.fields['bal_recd']
        self.fields['bal_amount']
        self.fields['keys_sent']
        self.fields['sec_retn']
        self.fields['booking_status']
        self.fields['booking_notes']
        self.fields['bkd_adult']
        self.fields['bkd_child']
        
    class Meta(BookingCreateForm.Meta):
        # show all the fields!
        fields = [
            'guest',
            'guest_status',
            'ack_date',
            'start_date',
            'end_date',
            'dep_recd',
            'bal_amount',
            'dep_amount',
            'sec_recd',
            'bal_recd',
            'keys_sent',
            'sec_retn',
            'booking_status',
            'booking_notes',
            'bkd_child',
            'bkd_adult',
            'guest_one',
            'guest_two',
            'guest_three',
            ]     
