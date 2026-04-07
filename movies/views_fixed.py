from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Showtime, Seat, Booking

@login_required
def get_showtime_seats(request, showtime_id):
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    seats = Seat.objects.filter(theater=showtime.theater).order_by('row', 'number')
    
    # Get booked seats
    booked_seats = set(Booking.objects.filter(
        showtime=showtime
    ).values_list('seats__id', flat=True))
    
    seats_data = [{
        'number': seat.number,
        'row': seat.row,
        'status': 'occupied' if seat.id in booked_seats else 'available'
    } for seat in seats]
    
    return JsonResponse({'seats': seats_data}) 