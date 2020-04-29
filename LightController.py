#from blinkt import set_pixel, set_brightness, show, clear
from collections import OrderedDict
import itertools

def SetupLights(rainyDays):
    #clear()
    SetupMorningLights(rainyDays[0])
    SetupEveningLights(rainyDays[1])
    #set_brightness(0.1)
    #set_pixel(0, 255, 255, 255)
    #show()

def SortDays(rainyDays):
    ordered =  OrderedDict(sorted(rainyDays.items()))
    return dict(itertools.islice(ordered.items(), 4))

def SetupMorningLights(morningDays):
    days = SortDays(morningDays)
    for i in range(len(days)):
        if(list(days.values())[i] == '1'):
            #set_pixel(i+1, 0, 255, 0)
            print("Setting Pixel " + str(i*2) + " With Rain")
        else:
            #set_pixel(i+1, 0, 0, 255)
            print("Setting Pixel " + str(i*2) + " Without Rain")

def SetupEveningLights(eveningDays):
    days = SortDays(eveningDays)
    for i in range(len(days)):
        if(list(days.values())[i] == '1'):
            #set_pixel(i+1, 0, 255, 0)
            print("Setting Pixel " + str(i*2+1) + " With Rain")
        else:
            #set_pixel(i+1, 0, 0, 255)
            print("Setting Pixel " + str(i*2+1) + " Without Rain")