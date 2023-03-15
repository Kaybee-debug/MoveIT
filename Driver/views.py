from django.shortcuts import render,redirect
from .models import Vihicle
# from .form import BookingForm

# Create your views here.
def displayVihicle(request):
    
    items = Vihicle.objects.all()
    
    context = {
        "items":items
    }
    
   
   
    return render(request,"displayVihicle.html",context)
