import BlynkLib
from time import sleep
import time
import random
import google_maps as gm
from sense_hat import SenseHat

sense = SenseHat()

temp = sense.get_temperature()
pressure = sense.get_pressure()
location = gm.get_location(52.244483, -7.144931)
humidity = sense.get_humidity()
direction = get_direction()

def get_direction():
    # Source: https://projects.raspberrypi.org/en/projects/compass-maze/2
    val = sense.get_compass()
    
    if (val < 45 or val > 315):
        sense.show_letter('N')
        return "North"
        
    elif (val < 135):
        sense.show_letter('E')
        return "East"
        
    elif (val < 225):
        sense.show_letter('S')
        return "South"
        
    else:
        sense.show_letter('W')
        return "West"

BLYNK_AUTH = 'key'

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    blynk.virtual_write(0, temp)
    blynk.virtual_write(1,pressure)
    blynk.virtual_write(3,location)
    blynk.virtual_write(4,humidity)
    blynk.virtual_write(5,get_direction())
    time.sleep(5)
    print("Temp: ", temp)
    print("Pressure: ", pressure)
    print("Location: ", location)
    print("Humidity: ", humidity)
    print("Direction (NESW): ", get_direction())
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    
