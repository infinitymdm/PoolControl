from django.shortcuts import render
from django.utils import timezone
from .forms import Schedule_Form, User_Settings_Form
from .models import Sensor_Info, Schedule, User_Settings

# Define the Title for the webpage that will show up on the tab
meta = {"title" : "Goober Pool Control"}
schedules = Schedule.objects.all()

def home(request):
    init_data = {'pump_state_start' : timezone.now()}   # Initial data for the form
    form = User_Settings_Form(request.POST or None, initial=init_data)   # Get the form if it has been posted

    # If the form is valid, save it to the database
    if form.is_valid():
        settings = form.save(commit=False)                              # Grab the user settings object
        prev_pump_state = User_Settings.objects.latest('id').pump_state # Get the previous pump state from the database
        curr_pump_state = settings.pump_state                           # Get the current pump state from the form data

        # If the pump state has not changed, don't reset the pump start time
        if prev_pump_state == curr_pump_state:
            settings.pump_state_start = User_Settings.objects.latest('id').pump_state_start
            form = settings
        User_Settings.objects.all().delete()                            # Delete the old db entry
        form.save()                                                     # Save the new db entry
        form = User_Settings_Form()                                     # Set up to show a blank form

    sensor_obj = Sensor_Info.objects.get(id=1)
    sensor_data = {
            'water_temp': sensor_obj.water_temp_sensed,
            'air_temp': sensor_obj.air_temp_sensed,
    }
    user_settings_obj = User_Settings.objects.latest('id')
    pump_duration = timezone.now() - user_settings_obj.pump_state_start
    user_settings_data = {
            'water_temp_desired': user_settings_obj.water_temp_desired,
            'pump_state': user_settings_obj.pump_state,
            'heater_state': user_settings_obj.heater_state,
            'pump_state_duration': pump_duration,
            'current_time': timezone.now(),
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
    
