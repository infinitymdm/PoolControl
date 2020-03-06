# Generated by Django 3.0.3 on 2020-03-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_temp_sensed', models.IntegerField(default=0)),
                ('air_temp_sensed', models.IntegerField(default=0)),
                ('water_pH_sensed', models.FloatField(default=0.0)),
                ('water_sanitizer_sensed', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='User_Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_temp_desired', models.IntegerField(default=0)),
                ('filter_pump_state', models.BooleanField(default=False)),
                ('heater_state', models.BooleanField(default=False)),
            ],
        ),
    ]
