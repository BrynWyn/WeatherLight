import time
import LightController
from weatherModule import WeatherModule
class main:
    def __init__(self):
        weather = WeatherModule()
        #Continuous For Loop.
        while True:
            response = weather.RunWeather()
            #Modify lights based on response.
            LightController.SetupLights(response)
            #This should be moved to the config.json.
            time.sleep(1800)    
main()