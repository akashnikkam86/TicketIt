from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from movies.models import Seat

class Command(BaseCommand):
    help = 'Cleans up seats that have been in reserved state for too long'

    def handle(self, *args, **options):
        # Find payments that are pending and older than 15 minutes
        cutoff_time = timezone.now() - timedelta(minutes=15)
        stale_payments = Payment.objects.filter(
            status='pending',
            created_at__lt=cutoff_time
        )

        # Release seats from stale payments
        for payment in stale_payments:
            payment.booking.seats.filter(status='reserved').update(status='available')
            payment.status = 'failed'
            payment.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Released seats for payment {payment.id} and marked as failed'
                )
            )

        # Also find any seats that are somehow still reserved without a pending payment
        orphaned_reserved_seats = Seat.objects.filter(
            status='reserved',
            booking__payment__isnull=True
        )
        orphaned_reserved_seats.update(status='available')
        
        if orphaned_reserved_seats.exists():
            self.stdout.write(
                self.style.SUCCESS(
                    f'Released {orphaned_reserved_seats.count()} orphaned reserved seats'
                )
            ) 