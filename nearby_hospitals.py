from selenium import webdriver
import requests
from geopy.geocoders import Nominatim
#This displays the map of available hosptals
import requests
from bs4 import BeautifulSoup

def hos_avai_map():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/maps')
        get_curr_onclick()
        location_url = f'https://www.google.com/maps/search/hospitals/@{latitude},{longitude},17z'
        driver.get(location_url)
        driver.implicitly_wait(10)
        
        try:
            input("Press Enter to close the browser...")
        except KeyboardInterrupt:
            pass
    except:
        return    
        driver.quit()



#This returns Available hospitals list in a dictionary
def availabe_display():
# Your Google Places API Key
    api_key = 'YOUR_API_KEY'
    get_cur_loclick()
    radius_km = 5  # Change this value to your desired radius in kilometers
    radius_meters = radius_km * 1000
    place_type = 'hospital'
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius_meters}&type={place_type}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        if results:
            print("Nearby Hospitals:")
            d=dict()
            for place in results:
                name = place.get('name', 'N/A')
                address = place.get('vicinity', 'N/A')
                d[name]=[address]
                print(f"Name: {name}, Address: {address}")
        else:
            print("No hospitals found nearby.")
    else:
        print(f"Error: {response.status_code}")
    return d    
def alert(address,value):
    if value==1:
        #alert due to heavy traffic
        #FETCH ACTUAL POLICE EMAIL  BUT HERE WE ARE USING A DUMMY EMAIL
        police=sollutionscode@gmail.com
        msg="There is an ambulance going to "+address+"\nIts current location is: "get_curr_loclick()+"\nplease help in making a lane free"
        sendmail_police(police,msg)
    if value==2:
        msg="ALERT!!!!\nThere is a severe medial emergency Ambulance is going to "+address
        msg+="\nIts current location is "+get_curr_loclick()
        sendmail_police(police,msg)
       
#***************CALL EMAIL MODULE******************#



#the current location will be shared for every 5 min
def onEmergency(hospital_address):

            get_curr_loclick()
            # Your Google Maps Directions API Key
            api_key = 'YOUR_API_KEY'
            geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={hospital_address}&key={api_key}'
            geocoding_response = requests.get(geocoding_url)

            if geocoding_response.status_code == 200:
                geocoding_data = geocoding_response.json()
                hospital_location = geocoding_data.get('results')[0]['geometry']['location']
                destination_latitude = hospital_location['lat']
                destination_longitude = hospital_location['lng']

                # Construct the URL for directions with traffic information
                url = f'https://maps.googleapis.com/maps/api/directions/json?origin={latitude},{longitude}&destination={destination_latitude},{destination_longitude}&key={api_key}&traffic_model=best_guess&departure_time=now'

                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    routes = data.get('routes', [])

                    if routes:
                        # Extract and print information about the first route
                        route = routes[0]
                        duration_in_traffic = route['legs'][0]['duration_in_traffic']['text']
                        traffic_condition = route['legs'][0]['duration_in_traffic']['text']
                        print(f"Duration in Traffic: {duration_in_traffic}")
                        print(f"Traffic Condition: {traffic_condition}")
                        if "Heavy traffic on your route":
                            alert(hospital_address,1)
                    else:
                        print("No routes found.")
                else:
                    print(f"Error: {response.status_code}")
            else:
                print(f"Error in geocoding: {geocoding_response.status_code}")

        #mail the location to nearest police station 



# Create a geocoder instance
def fetch_latitude(address):
    geolocator = Nominatim(user_agent="geoapiExercises")

    location = geolocator.geocode(address)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return [location.latitude,location.longitude]
    else:
        print("Location not found.")


        
def address_to_url(address):
    try:
        return "https://www.google.com/maps?q="+address
    except:
        print("Location not found.")        



