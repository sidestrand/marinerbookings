import datetime
from django import forms
from .models import Booking, Guest

from localflavor.gb.forms import GBPostcodeField, GBCountySelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import FormActions, AppendedText, PrependedText

common_guests = Layout(
    Div(
        Fieldset(
            'Guest details',
            Field('first_name', autofocus=True),
            'last_name',
            'email',
            'landline',
            'mobile'
            ),
        ),
    )

common_bookings = Layout(
    Div(
        Fieldset(
            '',
            Field('guest_one'),
            Field('guest_two'),
            Field('guest_three')
            ),
                css_class='col-md-4'),
    Div(
        Fieldset(
            '',
            Field('dep_recd', placeholder='dd/mm/yyyy'),
            Field('bal_recd', placeholder='dd/mm/yyyy'),
            Field('sec_recd', placeholder='dd/mm/yyyy'),
            Field('keys_sent', placeholder='dd/mm/yyyy'),
            Field('sec_retn', placeholder='dd/mm/yyyy')
            ),
                css_class='col-md-4'),
    Div(
        Fieldset(
            '',
            Field('notes')
            ),
                css_class='col-md-4'),
    )

common_new_enq = Layout(
    Div(
        Fieldset(
            '',
            Field('guest', autofocus=True),
            'guest_status'
            ),
                css_class='col-md-4'),
    Div(
        Fieldset(
            '',
            'bkd_adult',
            'bkd_child'
            ),
                css_class='col-md-4'),
    Div(
        Fieldset(
            '',
            Field('ack_date', placeholder='dd/mm/yyyy'),
            Field('start_date', placeholder='dd/mm/yyyy'),
            Field('end_date', placeholder='dd/mm/yyyy')
            ),
                css_class='col-md-4'),
    )


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
            # 'booking_source   ',
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
    
    ack_date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
    
    start_date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
        
    end_date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_id = 'add-booking'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-6'
        self.helper.help_text_inline = True
        self.helper.error_text_inline = True
        self.helper.layout = Layout(
            common_new_enq,
            FormActions(
                Submit('submit', "Save changes"),
                Button('cancel', "Cancel", onclick='history.go(-1);'),
                )
            )
    
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
    
    dep_recd = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
    
    bal_recd = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
        
    keys_sent = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
        
    sec_retn = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
    
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
        
        def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)

            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_id = 'add-booking'
            self.helper.form_class = 'form-horizontal'
            self.helper.label_class = 'col-md-4'
            self.helper.field_class = 'col-md-6'
            self.helper.help_text_inline = True
            self.helper.error_text_inline = True
            self.helper.layout = Layout(
                common_new_enq,
                common_bookings,
                FormActions(
                    Submit('submit', "Save changes"),
                    Button('cancel', "Cancel", onclick='history.go(-1);'),
                    )
                )

        
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
