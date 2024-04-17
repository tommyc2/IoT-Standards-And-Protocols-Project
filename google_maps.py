import googlemaps
import re
from faker import Faker
from time import sleep
from haversine import haversine, Unit
import database

total_journey_distance = 0

fake = Faker()

# Generating fake GPS data to replace GPS module
Faker.seed(5)

api_key = "key"
gm = googlemaps.Client(key=api_key)

def get_location():
    global total_journey_distance

    gps_data = str(fake.local_latlng())
    formatted = re.findall("[-\d\.]+", gps_data)
    lat1 = float(formatted[0])
    long1 = float(formatted[1])

    sleep(2)

    gps_data2 = str(fake.local_latlng())
    formatted2 = re.findall("[-\d\.]+", gps_data2)
    lat2 = float(formatted2[0])
    long2 = float(formatted2[1])

    distance = get_distance(lat1,long1,lat2,long2)
    total_journey_distance += distance
    #print("Journey distance so far: ",total_journey_distance, "km")
    database.save_distance(total_journey_distance)

    output = gm.reverse_geocode((lat2, long2))
    location = output[0]['formatted_address']

    return location

def get_distance(lat1,long1,lat2,long2):
    return int(haversine((lat1,long1),(lat2,long2), unit = Unit.KILOMETERS))

