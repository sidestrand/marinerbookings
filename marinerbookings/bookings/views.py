from django.shortcuts import render

from django.urls import reverse

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    TemplateView
    )
    
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail

from .models import Family, Booking, Guest

from .forms import GuestCreateForm, GuestUpdateForm, BookingCreateForm, BookingUpdateForm

class LandingView(LoginRequiredMixin, TemplateView):
    model = Booking

class GuestListView(LoginRequiredMixin, ListView):
    model = Guest
    
class GuestDetailView(LoginRequiredMixin, DetailView):
    model = Guest

class GuestCreateView(LoginRequiredMixin, CreateView):
    model = Guest
    form_class = GuestCreateForm
    
    def get_absolute_url(self):
        """Return absolute URL to the Guest Detail page."""
        return reverse(
            'guest-detail', kwargs={"slug": self.slug}
        )

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class GuestUpdateView(LoginRequiredMixin, UpdateView):
    model = Guest
    form_class = GuestUpdateForm
    
    def form_valid(self, form):
        # from_email = 'owners@marinersaldeburgh.com'
        # recipient_list = ['richard@darton-moore.co.uk',] # put your real email here
        # subject = 'Subject text'
        # message = 'This is the body of the email.'
        # send_mail(subject, message, from_email, recipient_list)
        return super(GuestUpdateView, self).form_valid(form)
    
    def get_absolute_url(self):
        """Return absolute URL to the Guest Detail page."""
        return reverse(
            'guest_detail', kwargs={"slug": self.slug}
        )

    action = "Update"

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    
class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingCreateForm

    def get_absolute_url(self):
        """Return absolute URL to the Booking Detail page."""
        return reverse(
            'booking-detail', kwargs={"slug": self.slug}
        )
        
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingUpdateForm
 
    def get_absolute_url(self):
        """Return absolute URL to the Booking Detail page."""
        return reverse(
            'booking-detail', kwargs={"slug": self.slug}
        )

    action = "Update"
    
class BookingDashboardView(LoginRequiredMixin, ListView):
    template_name = "bookings/dashboard.html"
    model = Booking
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deposit_item'] = Booking.booking_deposit.all()
        context['balance_item'] = Booking.booking_balance.all()
        context['security_due_item'] = Booking.booking_sec_recd.all()
        context['keys_sent_item'] = Booking.booking_keys_sent.all()
        context['security_returned_item'] = Booking.booking_sec_returned.all()
        return context
    
class BookingDepositDueView(LoginRequiredMixin, ListView):
    queryset = Booking.booking_deposit.all()
    
class BookingBalanceDueView(LoginRequiredMixin, ListView):
    queryset = Booking.booking_balance.all()
    
class BookingSecurityDepRecd(LoginRequiredMixin, ListView):
    queryset = Booking.booking_sec_recd.all()
    
class BookingKeysSent(LoginRequiredMixin, ListView):
    queryset = Booking.booking_keys_sent.all()
    
class BookingSecReturned(LoginRequiredMixin, ListView):
    queryset = Booking.booking_sec_returned.all()    

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
        
class BookingFutureView(LoginRequiredMixin, ListView):
    queryset = Booking.future_bookings.all()

def print_bookings(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="booking_list.pdf"'

    buffer = io.BytesIO()

    report = BookingListPDF(buffer, 'A4')
    pdf_list = report.print_bookings()

    response.write(pdf_list)
    return response
