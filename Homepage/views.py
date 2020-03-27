from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import Schedule_Form
from .forms import Sensor_Info_Form
from .models import Sensor_Info

#class HomeView(TemplateView):
#    template_name = 'home.html'
#    def get(self, request):
#        sensorForm = Sensor_Info_Form()
#        sensorData = Sensor_Info.objects.all()
#        context = {
#        'water_temp_sensed': sensors,
#        'air_temp_sensed': sensors
#    }
#        return render(request, self.template_name, context)
def home(request):
    return render(request, 'home.html')

def schedule(request):
    form = Schedule_Form(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        "meta" : {"title" : "Goober Pool Control"}
    }
    return render(request, 'schedule.html', context)
##    return render(request, "schedules/create_schedule.html",context)
#    return HttpResponse('Welcome to the Schedule Page')

def thermostat(request):
    return render(request, 'thermostat.html', { "meta" : {"title" : "Goober Pool Control"} })
#    return HttpResponse('Welcome to the Thermostat Page')

def water_info(request):
    return render(request, 'water_info.html', { "meta" : {"title" : "Goober Pool Control"} })
#    return HttpResponse('Welcome to the Water Info Page')
    
