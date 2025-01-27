from django.db import models
from datetime import time

class BookATable(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    booking_date = models.DateField()  # Default removed; provide input in views or form
    booking_time = models.TimeField()  # Default removed; provide input in views or form
    guest_count = models.PositiveIntegerField(default=1)  # Enforced positive integers
    phone = models.CharField(max_length=15)
    special_requests = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return f"Booking by {self.first_name} {self.last_name} on {self.booking_date} at {self.booking_time}"

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"Message from {self.name} - {self.subject[:50]}..."  # Truncate subject if too long
