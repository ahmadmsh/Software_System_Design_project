import random
class WindSensor:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_wind_gust(self):
        # Replace this with actual code to read the temperature from the sensor
        # For simplicity, let's assume it returns a random temperature between 0 and 100
        wind_gust=[]
        for i in range(1,25):
            wind_gust.append(random.randint(0,50))
            wind_gustfinal=wind_gust[-1]  
        return wind_gustfinal, wind_gust
    
    def get_wind_direction(self):
        # Replace this with actual code to read the temperature from the sensor
        # For simplicity, let's assume it returns a random temperature between 0 and 100
        direction = ["North", "South", "East", "West", "Northeast", "Northwest", "Southeast", "Southwest"]
        
        return direction[round(random.uniform(0, 7))]
    
 
        


