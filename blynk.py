import blynklib
from time import sleep
import time
import random
import google_maps
#from sense import SenseHat

#temp = sense.get_temperature()
#pressure = sense.get_pressure()
#speed = google_maps.get_speed()


BLYNK_AUTH = 'VHEbUi6uPpCsSVG5i2i4gHNQu_mrWf-H'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    #blynk.virtual_write(0, temp)
    #blynk.virtual_write(1,pressure)
    temp = random.choice([27,24,23,20])
    blynk.virtual_write(2,temp)
    #time.sleep(.5)
    #print("Temp: ", temp)
    #print("Pressure: ", pressure)
    print("Speed: ",temp)
    #location = google_maps.get_location(52.250752, -7.137676)
    #blynk.virtual_write(3,location) # e.g paddy brownes road
    #time.sleep(1)
    #print("Location: ",location)
    
