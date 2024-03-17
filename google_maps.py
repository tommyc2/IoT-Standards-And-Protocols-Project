import googlemaps

gm = googlemaps.Client(key="API_KEY")

def get_location(lat,long):
    output = gm.reverse_geocode((lat, long))

    location = output[0]['formatted_address']
    return location

print("Current location: ",get_location(52.172865, -7.510142))