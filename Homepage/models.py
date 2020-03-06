from django.db import models

# Create your models here.

## User Settings to Display on the UI and use in determining control of equipment

# Define User_Settings model
class User_Settings(models.Model):
    water_temp_desired = models.IntegerField(default = 0)
    filter_pump_state = models.BooleanField(default = False)
    heater_state = models.BooleanField(default = False)
#    set_schedule = schedule()

    def __str__(self):
        return 'Pump ON: ' + str(self.filter_pump_state) + ', Heater ON: ' + str(self.heater_state)

# Define Sensor_Info model
class Sensor_Info(models.Model):
    water_temp_sensed = models.IntegerField(default = 0)
    air_temp_sensed = models.IntegerField(default = 0)
    water_pH_sensed = models.FloatField(default = 0.0)
    water_sanitizer_sensed = models.FloatField(default = 0.0)


