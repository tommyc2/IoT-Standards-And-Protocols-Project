import googlemaps
import requests
import time

api_key = "API_KEY"
gm = googlemaps.Client(key=api_key)

regional_road = [52.244483, -7.144931]

def get_location(lat,long):
    output = gm.reverse_geocode((lat, long))

    location = output[0]['formatted_address']
    return location

def get_speed():
    return abs(25)

def analyse_braking():
    s1 = get_speed()
    time.sleep(3)
    s2 = get_speed()


#print(get_location(regional_road[0],regional_road[1]))