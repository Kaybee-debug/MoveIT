from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.service,name="service"),
    path("add/",views.add_bookings,name="add"),
    path("display/",views.displayBookings,name="display"),
    # path('courseDetail/', views.courseDetail,name="courseDetail"),
    # path('moduleDetail/', views.moduleDetail,name="moduleDetail"),
    # path('listing/', views.listing,name="listing"),
    
    
    
]