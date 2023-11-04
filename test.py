from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Start a web driver (Chrome in this example)
driver = webdriver.Chrome()

# URL of the webpage you want to scrape
url = 'https://www.gps-coordinates.net/my-location'

# Open the webpage with the web driver
driver.get(url)

# Wait for a few seconds to allow the page to load
driver.implicitly_wait(10)

# Handle pop-ups or redirects if needed
# Example: Accept cookies pop-up
try:
    accept_cookies = driver.find_element(By.ID, 'accept-cookies')
    accept_cookies.click()
except Exception as e:
    pass

# If the page has a search form, fill it and simulate a user interaction
# Example: Search for a location
try:
    search_input = driver.find_element(By.ID, 'search-input')
    search_input.send_keys('Your Location')
    search_input.send_keys(Keys.RETURN)
except Exception as e:
    pass

# Wait for the page to stabilize after interactions
# Example: Wait for an element to become visible
wait = WebDriverWait(driver, 10)
element1 = wait.until(EC.visibility_of_element_located((By.ID, 'lat')))
element2 = wait.until(EC.visibility_of_element_located((By.ID, 'lon')))

# Get the page source
page_source = driver.page_source

# Create a BeautifulSoup object to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find the element with the id "lat"
element1 = soup.find(id='lat')
element2=soup.find(id="lon")

if element1:
    # Print the text content of the element
    print("latitude")
    print(element1.text)
elif element2:
    print("longitude")
    print(element2.text)    

else:
    print("Element with id 'lat' not found")

# Close the web driver
driver.quit()
