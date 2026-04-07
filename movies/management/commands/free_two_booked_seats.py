from django.core.management.base import BaseCommand
from movies.models import Seat

class Command(BaseCommand):
    help = 'Frees up (sets as available) any two booked seats.'

    def handle(self, *args, **options):
        booked_seats = Seat.objects.filter(status='booked')[:2]
        if not booked_seats:
            self.stdout.write(self.style.WARNING('No booked seats found.'))
            return
        for seat in booked_seats:
            seat.status = 'available'
            seat.save()
            self.stdout.write(self.style.SUCCESS(f'Seat {seat} set to available.')) 