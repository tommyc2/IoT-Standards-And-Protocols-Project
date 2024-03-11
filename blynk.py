import BlynkLib
from time import sleep
import requests
import time
import random

api_key = "5b2ddccbcc8054d447c55ed535cf8928"
link = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q=dungarvan,Ireland&APPID={api_key}"
data = requests.get(link).json()

#Data
temp = data['main']['temp']
pressure = data['main']['pressure']


BLYNK_AUTH = 'VHEbUi6uPpCsSVG5i2i4gHNQu_mrWf-H'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# register handler for virtual pin V0 write event
while True:
    blynk.run()
    blynk.virtual_write(0, temp)
    blynk.virtual_write(1,pressure)
    blynk.virtual_write(2,random.choice([27,24,23,20]))
    time.sleep(.5)
    print("Temp: ", temp)
    print("Pressure: ", pressure)
    print("Speed: ",random.choice([27,24,23,20]))
