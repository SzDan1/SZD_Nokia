from datetime import datetime
import math

def parking_Calc(entry, exit):
    if entry < exit:
        return "Hibás bemenet"
    minute = int((entry-exit).total_seconds()/60)
    if minute >= 1440:
        return 10000
    if minute <= 30:
        return 0
    minute -= 30
    fee = 0
    fee += math.ceil(min(minute,180)/60)*300
    minute -= min(minute,180)
    if minute > 0:
        fee += math.ceil(minute/60)*500
    return fee

with open("parking_calculator/input.txt") as inp, open("output.txt", "w") as out:
    next(inp) 
    next(inp)
    for row in inp:
        plate, ent_date, ent_time, ex_date, ex_time = row.split("    ")
        