from django.shortcuts import render

from .forms import Schedule_Form
from .models import Sensor_Info

# Define the Title for the webpage that will show up on the tab
meta = {"title" : "Goober Pool Control"}

sensorObj = Sensor_Info.objects.get(id=1)
sensorData = {
        'water_temp': sensorObj.water_temp_sensed,
        'air_temp': sensorObj.air_temp_sensed,
}

def home(request):
    context = {
        'sensorData' : sensorData,
        'meta' : meta
    }
    return render(request, 'home.html', context)

def schedule(request):
    form = Schedule_Form(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        'meta' : meta
    }
    return render(request, 'schedule.html', context)

def thermostat(request):
    return render(request, 'thermostat.html', { "meta" : meta })

def water_info(request):
    return render(request, 'water_info.html', { "meta" : meta })
    
