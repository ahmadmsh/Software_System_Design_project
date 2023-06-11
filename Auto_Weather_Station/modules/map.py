from PyQt5 import  QtWebEngineWidgets
import json

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        coords_dict = json.loads(msg)
        coords_lat = coords_dict['geometry']['coordinates'][0]
        coords_lon = coords_dict['geometry']['coordinates'][1]
        print(str(coords_lat) + " " + str(coords_lon))

    