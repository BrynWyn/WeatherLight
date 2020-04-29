#from blinkt import set_pixel, set_brightness, show, clear
from collections import OrderedDict

def SetupLights(rainyDays):
    #clear()
    SetupMorningLights(rainyDays[0])
    SetupEveningLights(rainyDays[1])
    a = SortDays(rainyDays)
    set_brightness(0.1)
    #set_pixel(0, 255, 255, 255)
    show()
    print(a)

def SortDays(rainyDays):
    return OrderedDict(sorted(rainyDays.items()))

def SetupMorningLights(morningDays):
    days = SortDays(morningDays)
    for i in range(len(days)):
        set_pixel(i+1, 255, 255, 255)
        print("Setting Pixel " + str(i*2))

def SetupEveningLights(eveningDays):
    days = SortDays(eveningDays)
    for i in range(len(days)):
        set_pixel(i+1, 255, 255, 255)
        print("Setting Pixel " + str((i*2)+1))