from django.db import models

# Create your models here.

class Booking(models.Model):
    location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField(null=True)
    time =models.TimeField(auto_now_add=True)
   
    def __str__(self): 
        return self.location  
