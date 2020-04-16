from django.db import models
from datetime import datetime, timezone

# Create your models here.

## User Settings to Display on the UI and use in determining control of equipment

# Define User_Settings model
class User_Settings(models.Model):
    water_temp_desired = models.IntegerField(default = 0)
    pump_state = models.BooleanField(default = False)
    heater_state = models.BooleanField(default = False)
    pump_state_start = models.DateTimeField(default= datetime.now(timezone.utc))
    def __str__(self):
        return 'Pump ON: ' + str(self.pump_state) + ', Heater ON: ' + str(self.heater_state)


class Schedule(models.Model):
    name = models.CharField(max_length=100)
    turn_heater_on = models.BooleanField(default= False)
    # if heater, what temp?
    turn_on_time = models.TimeField(default= datetime.now().time())
    turn_off_time = models.TimeField(default= datetime.now().time())
    Sunday = models.BooleanField(default= False)
    Monday = models.BooleanField(default= False)
    Tuesday = models.BooleanField(default= False)
    Wednesday = models.BooleanField(default= False)
    Thursday = models.BooleanField(default= False)
    Friday = models.BooleanField(default= False)
    Saturday = models.BooleanField(default= False)
    # If false, the schedule will be deleted when the turn_off_time has been reached.
    repeat = models.BooleanField(default=True)

# Define Sensor_Info model
class Sensor_Info(models.Model):
    water_temp_sensed = models.IntegerField(default = 0)
    air_temp_sensed = models.IntegerField(default = 0)
    water_pH_sensed = models.FloatField(default = 0.0)
    water_sanitizer_sensed = models.FloatField(default = 0.0)

    def __str__(self):
        return 'Temp Sensed: Water: ' + str(self.water_temp_sensed) + ', Air: ' + str(self.air_temp_sensed)
