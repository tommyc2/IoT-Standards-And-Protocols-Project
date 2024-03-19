import googlemaps
import requests
import time

api_key = "key"
gm = googlemaps.Client(key=api_key)

regional_road = [52.244483, -7.144931]

def get_location(lat,long):
    output = gm.reverse_geocode((lat, long))

    location = output[0]['formatted_address']
    return location


#print(get_location(regional_road[0],regional_road[1]))
