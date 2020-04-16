from django import forms

from .models import User_Settings, Sensor_Info, Schedule

class User_Settings_Form(forms.ModelForm):
    class Meta:
        model = User_Settings
        fields = [
            'pump_state',
            'heater_state',
            'pump_state_start'
        ]
        widgets = { 'pump_state_start': forms.HiddenInput() }


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
            'turn_heater_on',
            #'heater_temp',
            'turn_on_time',
            'turn_off_time',
            'Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'repeat',
            ]