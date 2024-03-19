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

BLYNK_AUTH = 'key'

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    blynk.virtual_write(0, temp)
    blynk.virtual_write(1,pressure)
    blynk.virtual_write(3,location)
    time.sleep(5)
    print("Temp: ", temp)
    print("Pressure: ", pressure)
    print("Location: ", location)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    
