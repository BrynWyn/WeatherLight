import json
import requests

class WeatherModule:
    headers = {
        'res' : '3hourly',
        'key' : ''
    }

    rainCodes = {
        "8":"Overcast",
        "9":"Light rain shower (night)",
        "10":"Light rain shower (day)",
        "11":"Drizzle",
        "12":"Light rain",
        "13":"Heavy rain shower (night)",
        "14":"Heavy rain shower (day)",
        "15":"Heavy rain",
        "16":"Sleet shower (night)",
        "17":"Sleet shower (day)",
        "18":"Sleet",
        "19":"Hail shower (night)",
        "20":"Hail shower (day)",
        "21":"Hail",
        "22":"Light snow shower (night)",
        "23":"Light snow shower (day)",
        "24":"Light snow",
        "25":"Heavy snow shower (night)",
        "26":"Heavy snow shower (day)",
        "27":"Heavy snow",
        "28":"Thunder shower (night)",
        "29":"Thunder shower (day)",
        "30":"Thunder"
        }
    rainyDaysMorning = {}
    rainyDaysEvening = {}
    middlePeriod = 5

    def __init__(self):
        self.loadConfig()

    def loadConfig(self):
        with open("config.json","r") as json_data_file:
            configData = json.load(json_data_file)
            self.headers['key'] = configData["API"]["key"]
            self.apiBaseURL = configData["API"]["url"]+"/"+configData["API"]["format"]+"/"+configData["API"]["locationID"]

    def RunWeather(self):
        weatherJson = self.GetWeather()
        for days in weatherJson["SiteRep"]["DV"]["Location"]["Period"]:
            if(self.CheckForRainMorning(days) == True):
                self.rainyDaysMorning.update({days["value"]:'1'})
            else:
                self.rainyDaysMorning.update({days["value"]:'0'})
            
            if(self.CheckForRainEvening(days) == True):
                self.rainyDaysEvening.update({days["value"]:'1'})
            else:
                self.rainyDaysEvening.update({days["value"]:'0'})

        return [self.rainyDaysMorning, self.rainyDaysEvening]


    def CheckForRainMorning(self, days):
        count = 1
        for sections in days["Rep"]:

            rain = sections["W"] in self.rainCodes
            if(rain == True & count <= self.middlePeriod):
                return True

            count = count + 1

        return False

    def CheckForRainEvening(self, days):
        count = 1
        for sections in days["Rep"]:
            rain = sections["W"] in self.rainCodes
            if(rain == True & count > self.middlePeriod):
                return True
            count = count + 1
days
        return False

    def GetWeather(self):

        with open("TestData.json") as json_file:
            return json.load(json_file)
        
        response = requests.get(self.apiBaseURL,params=self.headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

