from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
import PyQt5.QtWebEngineWidgets as QtWebEngineWidgets
from . import map
import folium, io
from folium.plugins import Draw
from folium.plugins import MousePosition
from . import temp_sensor
import os
#from temp_sensor import TemperatureSensor
from . import pressure_sensor
#from pressure_sensor import PressureSensor
from . import wind
dir='C:/Users/mohfi/OneDrive/Desktop/Auto_Weather_Station/modules/'

class CreateSensor(QMainWindow):
    def __init__(self):
        super(CreateSensor, self).__init__()
        uic.loadUi(os.path.join(dir,'create_sensor.ui'), self)
        
        self.type_cb.addItem("Temperature")
        self.type_cb.addItem("Pressure")
        self.type_cb.addItem("Wind")
        
        self.type_cb.activated.connect(self.change_value_type)
        self.load_map_pb.clicked.connect(self.load_map)
        self.create_sensor_pb.clicked.connect(self.save_sensor) 
        self.cancel_sensor_pb.clicked.connect(self.close_window) 
        
    
    def change_value_type(self):
        type = self.type_cb.currentText()
        
        if(type == "Temperature"):
            self.model_cb.clear()
            self.model_cb.addItem("SHT31")
        
        elif (type == "Pressure"):
            self.model_cb.clear()
            self.model_cb.addItem("pr")
        
        else:
            self.model_cb.clear()
            self.model_cb.addItem("KW-2498")
    
    
    def load_map(self):
        self.m = folium.Map(location=[54.3520, 18.6466], zoom_start=13)
        formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        
        self.draw = Draw(
            draw_options={
                'polyline': False,
                'rectangle': True,
                'polygon': True,
                'circle': False,
                'marker': True,
                'circlemarker': False},
            edit_options={'edit': False},
            show_geometry_on_click=True)
        self.m.add_child(self.draw)
            
        MousePosition(
                position="topright",
                separator=" | ",
                empty_string="NaN",
                lng_first=True,
                num_digits=20,
                prefix="Coordinates:",
                lat_formatter=formatter,
                lng_formatter=formatter,
                ).add_to(self.m)
        
        
        self.data = io.BytesIO()
        self.m.save(self.data, close_file=False)
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.page = map.WebEnginePage(self.view)
        self.view.setPage(self.page)
        self.view.setHtml(self.data.getvalue().decode())
        self.view.show()
    
            
    def save_sensor(self):
        type = self.type_cb.currentText()
        model = self.model_cb.currentText()
        if(type == "Temperature"):
            temp_sensor1 = temp_sensor.TemperatureSensor("Living Room", "Main Building")
            [_,temperature] = temp_sensor1.get_temperature()
            with open(os.path.join(dir,'temp.txt'), 'w') as f:
                for x in temperature:
                    f.write(str(x)+' ')
                f.close()
                print("temp.txt file generated")
        elif(type == "Pressure"):
            pressure_sensor1 = pressure_sensor.PressureSensor("Living Room","Main Building")
            [_,pressure] = pressure_sensor1.get_pressure()
            with open(os.path.join(dir,'pressure.txt'), 'w') as f:
                for x in pressure:
                    f.write(str(x)+' ')
                f.close()
                print("pressure.txt file generated")
        else:
            wind_sensor1 = wind.WindSensor("Living Room","Main Building")
            [_,wind_gust] = wind_sensor1.get_wind_gust()
            with open(os.path.join(dir,'wind_gust.txt'), 'w') as f:
                for x in wind_gust:
                    f.write(str(x)+' ')
                f.close()
                print("wind_gust.txt file generated")
    def close_window(self):
        self.close()
        
