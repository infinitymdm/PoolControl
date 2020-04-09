from django.shortcuts import render

from .forms import Schedule_Form
from .models import Sensor_Info, Schedule, User_Settings

# Define the Title for the webpage that will show up on the tab
meta = {"title" : "Goober Pool Control"}

def home(request):
    sensor_obj = Sensor_Info.objects.get(id=1)
    sensor_data = {
            'water_temp': sensor_obj.water_temp_sensed,
            'air_temp': sensor_obj.air_temp_sensed,
    }
    context = {
        'sensor_data' : sensor_data,
        'meta' : meta
    }
    return render(request, 'home.html', context)

def schedule(request):
    schedules = Schedule.objects.all()
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
    
