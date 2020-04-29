from collections import OrderedDict

def SetupLights(rainyDays):
    a = SortDays(rainyDays)
    print(a)

def SortDays(rainyDays):
    return OrderedDict(sorted(rainyDays.items()))