from django.shortcuts import render
from django.db import models

from .forms import Schedule_Form, User_Settings_Form
from .models import Sensor_Info, Schedule, User_Settings
from datetime import datetime, timezone

# Define the Title for the webpage that will show up on the tab
meta = {"title" : "Goober Pool Control"}
schedules = Schedule.objects.all()

def home(request):
    form = User_Settings_Form(request.POST or None)
    if form.is_valid():
#        User_Settings.objects.all().delete()
        form.save()
        form = User_Settings_Form()

    sensor_obj = Sensor_Info.objects.get(id=1)
    sensor_data = {
            'water_temp': sensor_obj.water_temp_sensed,
            'air_temp': sensor_obj.air_temp_sensed,
    }
    user_settings_obj = User_Settings.objects.latest('id')
    pump_duration = datetime.now(timezone.utc) - user_settings_obj.pump_state_start
    user_settings_data = {
            'water_temp_desired': user_settings_obj.water_temp_desired,
            'pump_state': user_settings_obj.pump_state,
            'heater_state': user_settings_obj.heater_state,
            'pump_state_duration': pump_duration,
            'current_time': datetime.now(),
    }
    context = {
        'form' : form,
        'sensor_data' : sensor_data,
        'user_settings_data': user_settings_data,
        'meta' : meta,
    }
    return render(request, 'home.html', context)

def schedule(request):
    form = Schedule_Form(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form,
        'schedules' : schedules,
        'meta' : meta
    }
    return render(request, 'schedule.html', context)

def thermostat(request):
    return render(request, 'thermostat.html', { "meta" : meta })

def water_info(request):
    water_obj = Sensor_Info.objects.get(id=1)
    water_data = {
        'water_temp': water_obj.water_temp_sensed,
        'water_pH': water_obj.water_pH_sensed,
        'water_sanitizer': water_obj.water_sanitizer_sensed
    }
    context = {
        'water_data': water_data,
        'meta': meta
    }
    return render(request, 'water_info.html', context)
    
