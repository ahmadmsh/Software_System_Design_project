import random
class TemperatureSensor:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_temperature(self):
        # Replace this with actual code to read the temperature from the sensor
        # For simplicity, let's assume it returns a random temperature between 0 and 100
        temp=[]
        for i in range(1,25):
            temp.append(random.randint(-20,50))
            tempfinal=temp[-1]  
        return tempfinal, temp

 
        


