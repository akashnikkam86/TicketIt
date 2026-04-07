from django.contrib import admin
from .models import Movie, Theater, Showtime, Seat, Booking, Carousel

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'duration', 'rating']
    search_fields = ['title']
    list_filter = ['release_date', 'rating']

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity']
    search_fields = ['name', 'location']

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'start_time', 'price']
    list_filter = ['movie', 'theater', 'start_time']
    search_fields = ['movie__title', 'theater__name']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['theater', 'row', 'number', 'status']
    list_filter = ['theater', 'status']
    search_fields = ['theater__name', 'row']

def clear_all_bookings(modeladmin, request, queryset):
    from .models import Seat, Booking
    Booking.objects.all().delete()
    Seat.objects.all().update(status='available')
    modeladmin.message_user(request, "All bookings deleted and all seats set to available.")
clear_all_bookings.short_description = "Delete all bookings and reset all seats to available"

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'showtime', 'booking_time', 'total_price']
    list_filter = ['booking_time', 'showtime__movie']
    search_fields = ['user__username', 'showtime__movie__title']
    readonly_fields = ['booking_time']
    actions = [clear_all_bookings]

admin.site.register(Carousel)
