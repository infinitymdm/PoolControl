from django import forms

from .models import User_Settings
from .models import Sensor_Info
from .models import Schedule

class Sensor_Info_Form(forms.ModelForm):
    class Meta:
        model = Sensor_Info
        fields = [
            'water_temp_sensed',
            'air_temp_sensed',
            'water_pH_sensed',
            'water_sanitizer_sensed',
        ]

class Schedule_Form(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'name',
            #'equipment_type',
            #'heater_temp',
            #'turn_on_time',
            #'duration',
            #'days_of_operation',
            'repeat',
            ]