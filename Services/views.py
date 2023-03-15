from django.shortcuts import render,redirect
from .models import Booking
from .form import BookingForm

# Create your views here.
def displayBookings(request):
    
    items = Booking.objects.all()
    
    context = {
        "items":items
    }
    
   
   
    return render(request,"displayBookings.html",context)

def service(request):
    
    return render(request,'service.html') 

def add_bookings(request):
  
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    
    
    
    context = {
        "form":form
    }
   
    return render(request,"makeBookings.html",context)







