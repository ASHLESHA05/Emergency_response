import smtplib
import random
from sinch import Client
import requests
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
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('emergencyresponse80@gmail.com','uwbssbzandgpyrlv')
otpnum = str(random.randint(100000,999999))
def send_mail_otp(email):
    server.sendmail('emergencyresponse80@gmail.com',email,"your veification code for emergency response system app is\n\n"+otpnum)

def send_mail_alert(email,name,loc):
    string="I am "+name+"You are my emergency contact i need help...\nThis is my approximate location: "+loc
    server.sendmail('emergencyresponse80@gmail.com',email,string)

def send_mail_driver(email):
    string="Emergency ambulance has been booked \n patients location is: https://www.google.com/maps/search/?api=1&query=12.938424,77.534852"
    server.sendmail('emergencyresponse80@gmail.com',email,string+"\n\n\n\n@CodeHunters")


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
    query = f"{latitude},{longitude}"
    gmaps_url = base_url + query

    return gmaps_url
















def emergency_alert(email,name,phn):
    url=get_curr_loclick()
    string="I am "+name+"You are my emergency contact i need help...\nThis is my approximate location: "+url
    server.sendmail('emergencyresponse80@gmail.com',email,string)
    def send_message(msg,phn):
        sinch_client = Client(
            key_id="d5255600-1753-4942-821f-952c3689cf65",
            key_secret="1i.PtFfbe9Qe_-c6U6v6UJnmRI",
            project_id="c469d659-92b6-4761-a944-67565b3c0243")

        send_batch_response = sinch_client.sms.batches.send(
            body=msg,
            to=[phn],
            from_="+447520662372",
            delivery_report="none"
        )
        print(send_batch_response)
    send_message(string,phn)

emergency_alert("ashleshat5@gmail.com","ashu","+91 7483611935")



