from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    # path('courseDetail/', views.courseDetail,name="courseDetail"),
    # path('moduleDetail/', views.moduleDetail,name="moduleDetail"),
    # path('listing/', views.listing,name="listing"),
    
    
    
]