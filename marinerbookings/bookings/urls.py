# mariners3/guests/urls.py
from django.urls import path
from . import views

app_name = "bookings"

urlpatterns = [
    path(
        route='',
        view=views.LandingView.as_view(template_name                                                                                                                            ="bookings/index.html"),
        name='index'
    ),

    path(
        route='booking-add/',
        view=views.BookingCreateView.as_view(),
        name='booking_add'
    ),
    path(
        route='booking-detail/<slug:slug>/',
        view=views.BookingDetailView.as_view(),
        name='booking_detail'
    ),

    path(
        route='<slug:slug>/booking-update/',
        view=views.BookingUpdateView.as_view(),
        name='booking_update'

    ),

    path(
        route='guests',
        view=views.GuestListView.as_view(),
        name='guest_list'
    ),

    path(
        route='guest-add/',
        view=views.GuestCreateView.as_view(),
        name='guest_add'
    ),
    path(
        route='guest-detail/<slug:slug>/',
        view=views.GuestDetailView.as_view(),
        name='guest_detail'
    ),

    path(
        route='<slug:slug>/guest-update/',
        view=views.GuestUpdateView.as_view(),
        name='guest_update'

    ),

    path(
        route='dashboard/',
        view=views.BookingDashboardView.as_view(),
        name='dashboard_list'
    ),

    path(
        route='bookings/',
        view=views.BookingListView.as_view(),
        name='booking_list'
    ),

    path(
        route='deposit/',
        view=views.BookingDepositDueView.as_view(
        ),
        name='deposit'
    ),

    path(
        route='sec_due/',
        view=views.BookingSecurityDepRecd.as_view(
        ),
        name='sec_due'
    ),

    path(
        route='keys_sent/',
        view=views.BookingKeysSent.as_view(
        ),
        name='keys_sent'
    ),

    path(
        route='balance/',
        view=views.BookingBalanceDueView.as_view(
            template_name='booking_balance.html'
        ),
        name='balance'
    ),

    path(
        route='future/',
        view=views.BookingFutureView.as_view(
            template_name='booking_future.html'
        ),
        name='future'
    ),

    path(
        route='sec_retn/',
        view=views.BookingListView.as_view(
            template_name='security returned.html'),
        name='sec_retn'
    ),

    path(
        route='monitor/',
        view=views.BookingListView.as_view(
            template_name='monitor.html'),
        name='monitor'
    ),

    path(
        'pdf/',
        views.print_bookings,
        name='pdf'
    ),
]
