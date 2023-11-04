from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import keyboard
import time
import requests
#this function returns location url of goole maps
latitude=""
longitude=""


def get_curr_loclick():
    global latitude
    global longitude 
    chrome_options = Options()   # Initialize the web driver with the headless options
    chrome_options.add_argument('--window-size=2x2')  # Set window size

    # Initialize the web driver with the headless options
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://www.gps-coordinates.net/my-location'
    driver.get(url)
    driver.implicitly_wait(5)
    try:
        accept_cookies = driver.find_element(By.ID, 'accept-cookies')
        accept_cookies.click()
    except Exception as e:
        pass

    # If the page has a search form, fill it and simulate a user interaction
    try:
        search_input = driver.find_element(By.ID, 'search-input')
        search_input.send_keys('Your Location')
        search_input.send_keys(Keys.RETURN)
    except Exception as e:
        pass

    # Wait for the page to stabilize after interactions
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, 'lat')))

    # Get the page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    element_lat = soup.find(id='lat')
    if element_lat:
        latitude=element_lat.text
        print("Latitude:",latitude )
    else:
        print("Element with id 'lat' not found")
    element_lon = soup.find(id='lng')
    if element_lon:
        longitude= element_lon.text
        print("Longitude:",longitude)
    else:
        print("Element with id 'lon' not found")
    latitude=latitude[0:9]
    longitude=longitude[0:10]
    driver.quit()
    base_url = "https://www.google.com/maps/search/?api=1&query="
    query = f"{latitude} {longitude}"
    gmaps_url = base_url + query

    return gmaps_url
   

#this function returns address of current location
def get_curr_address():
    get_curr_loclick()
    geolocator = Nominatim(user_agent="reverse_geocoder")
    location = f"{latitude}, {longitude}"
    address = geolocator.reverse(location, exactly_one=True)
    if address:
        return(address.address)
    else:
        print("not found")



#to track live location
def dispalyliveloc():
    try:
            driver1 = webdriver.Chrome()
            url = 'https://www.google.com/maps'
            # Open Google Maps in the web driver
            driver1.get(url)
            # Wait for a few seconds to allow the page to load
            driver1.implicitly_wait(10)
            count=0;
        
            while True:
                get_curr_loclick()
                location_url = f"https://www.google.com/maps?q={latitude},{longitude}"
                driver1.get(location_url)
                if(count==3):
                    return
                count+=1    
                time.sleep(10)
            # Wait for a few seconds to allow the map to load with your location
            driver1.implicitly_wait(10) 
    except:
        return       


dispalyliveloc()

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
    api_key = ''
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


# def alert(address,value):
#     if value==1:
#         #alert due to heavy traffic
#         #FETCH ACTUAL POLICE EMAIL  BUT HERE WE ARE USING A DUMMY EMAIL
#         police="sollutionscode@gmail.com"
#         msg="There is an ambulance going to "+address+"\nIts current location is: "get_curr_loclick()+"\nplease help in making a lane free"
#         sendmail_police(police,msg)
#     if value==2:
#         msg="ALERT!!!!\nThere is a severe medial emergency Ambulance is going to "+address
#         msg+="\nIts current location is "+get_curr_loclick()
#         sendmail_police(police,msg)
       

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

def address_to_url(address):
    try:
        return "https://www.google.com/maps?q="+address
    except:
        print("Location not found.")        
