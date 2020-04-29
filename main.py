import time
import LightController
from weatherModule import WeatherModule
class main:
    def __init__(self):
        weather = WeatherModule()
        while True:
            response = weather.RunWeather()
            LightController.SetupLights(response)
            time.sleep(1800)    

main()