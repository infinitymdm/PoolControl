from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def schedule(request):
#    return render(request, 'schedule.html')
    return HttpResponse('Welcome to the Schedule Page')

def thermostat(request):
#    return render(request, 'thermostat.html')
    return HttpResponse('Welcome to the Thermostat Page')

def water_info(request):
#    return render(request, 'water_info.html')
    return HttpResponse('Welcome to the Water Info Page')
