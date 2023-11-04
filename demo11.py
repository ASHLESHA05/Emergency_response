import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key='AIzaSyAMfpWeT_ak2ffFWqlLbe9eFYRoVzlX2hU')

# Get the user's location based on their IP address
current_location = gmaps.geolocate()

# Print the current location
print("Current Location: Latitude={}, Longitude={}".format(current_location['location']['lat'], current_location['location']['lng']))
