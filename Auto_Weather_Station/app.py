from main import UI
from PyQt5.QtWidgets import QApplication
from modules.temp_sensor import TemperatureSensor
from modules.pressure_sensor import PressureSensor
from modules.wind import WindSensor
import sys
import os
dir='C:/Users/mohfi/OneDrive/Desktop/Auto_Weather_Station/modules/'

app = QApplication(sys.argv)
UIwindow = UI()
UIwindow.weather_forecast('Gdansk,PL')

if os.path.exists(os.path.join(dir, "temp.txt")):
    with open(os.path.join(dir, "temp.txt")) as f:
        temperature = f.read()
    temperature = temperature.split()
    temperature=[int(x) for x in temperature]
    temperature_final=temperature[-1]
    f.close()
# Create an instance of the TemperatureSensor class
else:
    temp_sensor = TemperatureSensor("Living Room", "Main Building")
# Get the temperature reading
    [temperature_final,temperature] = temp_sensor.get_temperature()
if os.path.exists(os.path.join(dir, "pressure.txt")):
    with open(os.path.join(dir, "pressure.txt")) as f:
        pressure=f.read()
    pressure=pressure.split()
    pressure=[int(x) for x in pressure]
    pressure_final=pressure[-1]
    f.close()
else:
    pressure_sensor = PressureSensor("Living Room","Main Building")
    [pressure_final,pressure] = pressure_sensor.get_pressure()
if os.path.exists(os.path.join(dir, "wind_gust.txt")):
    with open(os.path.join(dir, "wind_gust.txt")) as f:
        wind_gust=f.read()
    wind_gust=wind_gust.split()
    wind_gust=[int(x) for x in wind_gust]
    wind_gust_final=wind_gust[-1]
    wind_sensor = WindSensor("Living Room","Main Building")
    f.close()
else:
    wind_sensor = WindSensor("Living Room","Main Building")
    [wind_gust_final,wind_gust] = wind_sensor.get_wind_gust()

UIwindow.set_measure_values(temperature_final, pressure_final, wind_gust_final, wind_sensor.get_wind_direction())
hours=list(range(1,25))
temp_values_graph = dict(hr=hours,tp=temperature,pr=pressure)

UIwindow.plot(temp_values_graph['hr'], temp_values_graph['tp'], temp_values_graph['pr'])

UIwindow.show()
app.exec_()