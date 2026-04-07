from django.core.management.base import BaseCommand
from movies.models import Theater, Seat

class Command(BaseCommand):
    help = 'Creates 30 seats for a theater'

    def add_arguments(self, parser):
        parser.add_argument('theater_id', type=int, help='The ID of the theater to create seats for')

    def handle(self, *args, **options):
        theater_id = options['theater_id']
        theater = Theater.objects.get(id=theater_id)
        
        # Delete existing seats for this theater
        Seat.objects.filter(theater=theater).delete()
        
        # Create 30 seats (5 rows of 6 seats each)
        seats = []
        for row in ['A', 'B', 'C', 'D', 'E']:
            for number in range(1, 7):
                seats.append(Seat(
                    theater=theater,
                    row=row,
                    number=number,
                    status='available'
                ))
        
        # Bulk create all seats
        Seat.objects.bulk_create(seats)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created 30 seats for theater {theater.name}')) 