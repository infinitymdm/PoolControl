from django.db import models

# Create your models here.

## User Settings to Display on the UI and use in determining control of equipment

# Define User_Settings model
class User_Settings(models.Model):
    water_temp_desired = models.IntegerField(default = 0)
    pump_state = models.BooleanField(default = False)
    heater_state = models.BooleanField(default = False)
    # pump_state_time = needs to count up hr:min:sec to tell the user how long the pump has been in its current state

    def __str__(self):
        return 'Pump ON: ' + str(self.pump_state) + ', Heater ON: ' + str(self.heater_state)

class Schedule(models.Model):
    name = models.CharField(max_length=1000)
    # equipment_type = pump, heater, other?
    # if heater, what temp?
    # turn_on_time = timeOfDay
    # duration = length of time to be on
    # days_of_operation = Sunday,Monday,etc.
    # If true, the schedule will not be deleted. If false, this one schedule will delete itself once it has turned off following its duration.
    repeat = models.BooleanField(default=True)

# Define Sensor_Info model
class Sensor_Info(models.Model):
    water_temp_sensed = models.IntegerField(default = 0)
    air_temp_sensed = models.IntegerField(default = 0)
    water_pH_sensed = models.FloatField(default = 0.0)
    water_sanitizer_sensed = models.FloatField(default = 0.0)

    def __str__(self):
        return 'Temp Sensed: Water: ' + str(self.water_temp_sensed) + ', Air: ' + str(self.air_temp_sensed)
