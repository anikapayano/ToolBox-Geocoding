"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

from urllib.request import urlopen
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    #pprint(response_data)
    return response_data

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"
get_json(url)
#print(response_data["results"][0]["formatted_address"])


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    latitude = place_name["results"][0]["geometry"]["location"]["lat"]
    longitude = place_name["results"][0]["geometry"]["location"]["lng"]
    return latitude, longitude

get_lat_long(response_data)
Lat_and_Long = get_lat_long(response_data)
print(Lat_and_Long)

def get_url(place_name):
    name = []
    structure = "https://maps.googleapis.com/maps/api/geocode/json?address="
    name = place_name.split(' ')
    for word in name:
        if word == name[0]:
            structure += word
        else:
            structure += '%'
            structure += word
    return structure

get_url("Fenway Park")

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    urlbase = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat="
    urlbase += str(latitude)
    urlbase += '&lon='
    urlbase += str(longitude)
    urlbase += '&format=json'
    response_data = get_json(urlbase)
    station_name = response_data["stop"][0]["stop_name"]
    distance = response_data["stop"][0]["distance"]
    return station_name, distance

latitude = Lat_and_Long[0]
longitude =  Lat_and_Long[1]
get_nearest_station(latitude,longitude)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """

    url = get_url(place_name)
    data = get_json(url)
    lat, long = get_lat_long(data)
    return get_nearest_station(lat, long)


find_stop_near(input("Place Name or Address:"))
