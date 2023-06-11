import random
class PressureSensor:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_pressure(self):
        # Replace this with actual code to read the temperature from the sensor
        # For simplicity, let's assume it returns a random temperature between 0 and 100
        press=[]
        for i in range(1,25):
            press.append(random.randint(1,50))
            pressfinal=press[-1] 
        return pressfinal, press