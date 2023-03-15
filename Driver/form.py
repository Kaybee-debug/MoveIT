from django import forms
from .models import Vihicle,Drivers

class DriverForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = "__all__"
        
class vihcleForm(forms.ModelForm):
    class Meta:
        model = Vihicle
        fields = "__all__"        

