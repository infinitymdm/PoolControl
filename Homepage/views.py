from django.shortcuts import render
from django.db import models

from .forms import Schedule_Form, User_Settings_Form, Water_Temp_Form
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
        form = Schedule_Form()

    context = {
        'form' : form,
        'schedules' : schedules,
        'meta' : meta
    }
    return render(request, 'schedule.html', context)

def schedule_details(request, schedule_id):
    schedule_obj = Schedule.objects.get(id=schedule_id)
    context = {
        'schedule_object': schedule_obj,
    }
    return render(request, 'schedule_details.html', context)


def thermostat(request):
    form = Water_Temp_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = User_Temp_Form()
    sensor_obj = Sensor_Info.objects.latest('id')
    sensor_data = {
        'water_temp': sensor_obj.water_temp_sensed,
        'air_temp': sensor_obj.air_temp_sensed
    }
    current_time = datetime.now()
    context = {
        'user_temp_desired': form,
        'sensor_data': sensor_data,
        'current_time': current_time,
        'meta': meta
    }
    return render(request, 'thermostat.html', context)

def water_info(request):
    water_obj = Sensor_Info.objects.latest('id')
    water_data = {
        'water_temp': water_obj.water_temp_sensed,
        'water_pH': water_obj.water_pH_sensed,
        'water_sanitizer': water_obj.water_sanitizer_sensed
    }
    context = {
        'water_data': water_data,
        'meta': meta,
    }
    return render(request, 'water_info.html', context)
    
