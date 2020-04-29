from blinkt import set_pixel, set_brightness, show, clear
from collections import OrderedDict

def SetupLights(rainyDays):
    a = SortDays(rainyDays)
    set_brightness(0.1)
    set_pixel(0, 255, 255, 255)
    show()
    print(a)

def SortDays(rainyDays):
    return OrderedDict(sorted(rainyDays.items()))