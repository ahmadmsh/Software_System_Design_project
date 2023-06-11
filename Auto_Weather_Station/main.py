from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from modules.CreateSensor import CreateSensor
import pyowm
import os
dir='C:/Users/mohfi/OneDrive/Desktop/Auto_Weather_Station/'
own = pyowm.OWM('df5f6075a117d86404d5e3aadf1096be')


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(os.path.join(dir,'window.ui'), self)
        
        self.actionCreate_Sensor.triggered.connect(self.create_new_sensor)    
    
    # Get weather forecast         
    def weather_forecast(self, place):
        weather_mgr = own.weather_manager()
        observation = weather_mgr.weather_at_place(place).weather
        temp_dict_celsius = observation.temperature('celsius')
        self.forecast_info.setText(f'Temperature: {temp_dict_celsius["temp"]}°C')
    
    # set measure values from sensors    
    def set_measure_values(self, temp, pressure, wind_gust, direction):
        self.temperature_value.setText(f'{str(temp)}°C')
        self.pressure_value.setText(f'{str(pressure)} PA')
        self.wind_gust_value.setText(f'{str(wind_gust)} m/s')
        self.wind_direction_value.setText(f'{str(direction)}')
    
    # Plot the main Graphic
    def plot(self, hour, temperature, pressure):
        self.graphicsView.plot(hour, temperature)
        self.graphicsView.showGrid(True, True)
        self.graphicsView.addLegend()
       
        self.graphicsView.setLabel('left', 'Temperature °C / Pressure', units='Pa')
        self.graphicsView.setLabel('bottom', 'Time', units='s')
        
        self.graphicsView.plot(hour, temperature,  pen='b', symbol='o', symbolPen='b', symbolBrush=0.2, name='Temperature')
        self.graphicsView.plot(hour, pressure, pen='r', symbol='x', symbolPen='r', symbolBrush=0.2, name='Pressure')
    
    # Display the create sensor window
    def create_new_sensor(self):
        self.c_sensor = CreateSensor()
        self.c_sensor.show()
         
    
  
   
