from django.urls import path
from . import views

urlpatterns = [
    
    # Go to Schedule Page
    path('schedule/', views.schedule, name='schedule'),

    # Go to Thermostat Page
    path('thermostat/', views.thermostat, name='thermostat'),

    # Go to Water Info Page
    path('water_info/', views.water_info, name='water_info'),

    # Go to Homepage
    path('', views.home, name='home'),
]