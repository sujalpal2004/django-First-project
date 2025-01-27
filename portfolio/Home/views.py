from django.shortcuts import render
from Home.models import BookATable as TableModel
from Home.models import Contact as ContactModel  # Avoid conflict with function name
from django.contrib import messages  # For displaying success or error messages

# Create your views here.
def Home(request):
    """Renders the home page."""
    return render(request, 'Home.html')

def About(request):
    """Renders the about us page."""
    return render(request, 'About Us.html')

def Contact(request):
    """Handles the contact form submission."""
    if request.method == "POST":
        # Collect data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate data
        if not all([name, email, subject, message]):
            messages.error(request, "All fields are required.")
            return render(request, 'Contact Us.html')

        try:
            # Save to the database
            contacting = ContactModel(name=name, email=email, subject=subject, message=message)
            contacting.save()
            messages.success(request, "Thank you for your query, we will respond soon.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return render(request, 'Contact Us.html')

def BookATable(request):
    """Handles the booking table form submission."""
    if request.method == "POST":
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        guest_count = request.POST.get('guest_count')
        phone = request.POST.get('phone')
        special_requests = request.POST.get('special_requests')

        # Validate data
        if not all([first_name, last_name, booking_date, booking_time, guest_count, phone]):
            messages.error(request, "All fields except special requests are required.")
            return render(request, 'Book A Table.html')

        try:
            # Save to database
            booking = TableModel(
                first_name=first_name,
                last_name=last_name,
                booking_date=booking_date,
                booking_time=booking_time,
                guest_count=guest_count,
                phone=phone,
                special_requests=special_requests
            )
            booking.save()
            messages.success(request, "Your table has been booked successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred while booking your table: {e}")
            return render(request, 'Book A Table.html')

        return render(request, 'Book A Table.html', {'message': 'Your table has been booked successfully!'})

    return render(request, 'Book A Table.html')
