from django.shortcuts import render

from django.urls import reverse

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView
    )
    
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Family, Booking

from .forms import GuestCreateForm, GuestUpdateForm, BookingCreateForm, BookingUpdateForm

class GuestListView(LoginRequiredMixin, ListView):
    model = Booking
    
class GuestDetailView(LoginRequiredMixin, DetailView):
    model = Booking

class GuestCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingCreateForm
    
    def get_absolute_url(self):
        """Return absolute URL to the Guest Detail page."""
        return reverse(
            'guest-detail', kwargs={"slug": self.slug}
        )

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class GuestUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingUpdateForm
    
    def get_absolute_url(self):
        """Return absolute URL to the Guest Detail page."""
        return reverse(
            'guest-detail', kwargs={"slug": self.slug}
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

    def get_absolute_url(self):
        """Return absolute URL to the Booking Detail page."""
        return reverse(
            'booking-detail', kwargs={"slug": self.slug}
        )
    model = Booking
    form_class = BookingUpdateForm

    action = "Update"
