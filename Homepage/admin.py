from django.contrib import admin
from .models import User_Settings
from .models import Sensor_Info

admin.site.register(User_Settings)
admin.site.register(Sensor_Info)
