from django.db import models

# Create your models here.

class Drivers(models.Model):
    driverName = models.CharField(max_length=100)
    carRegistration= models.CharField(max_length=100)
    model= models.CharField(max_length=100)
  
    def __str__(self): 
        return self.driverName  
    

class Vihicle(models.Model):
    Trailer ='Trailer'
    Bakkie ='Bakkie'
    Truck ='Truck'
    transportationChoice = [
        (Trailer,'Trailer'),
        (Bakkie,'Bakkie'),
        (Truck ,'Truck')
    ]
    
    
    transportation = models.CharField(max_length=7,choices=transportationChoice, default=Trailer )  
    price = models.DecimalField(max_digits=6,decimal_places=2)
    weight = models.IntegerField()
    car_registration= models.ForeignKey(Drivers ,on_delete=models.PROTECT)
    
    
    def __str__(self): 
        return self.transportation
