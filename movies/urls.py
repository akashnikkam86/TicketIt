from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/book/', views.book_ticket, name='book_ticket'),
    path('bookings/', views.booking_history, name='booking_history'),
    path('bookings/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('bookings/invoice/<int:booking_id>/', views.booking_invoice, name='booking_invoice'),
    path('bookings/invoice/<int:booking_id>/pdf/', views.booking_invoice_pdf, name='booking_invoice_pdf'),
    path('api/showtime/<int:showtime_id>/seats/', views.get_showtime_seats, name='get_showtime_seats'),
    path('api/showtime/<int:showtime_id>/has_booking/', views.has_booking_for_showtime, name='has_booking_for_showtime'),
    path('api/movie/<int:movie_id>/book_seats/', views.ajax_book_seats, name='ajax_book_seats'),
    path('api/movie/<int:movie_id>/cancel_booking/', views.ajax_cancel_booking, name='ajax_cancel_booking'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_movies, name='search_movies'),
    path('payment/<int:booking_id>/', views.payment_page, name='payment_page'),
] 