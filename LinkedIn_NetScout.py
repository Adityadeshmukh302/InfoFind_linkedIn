from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Creating a webdriver instance which will be use to log into LinkedIn
driver = webdriver.Chrome("/Users/adityadeshmukh/Documents/Web crawler:scrapper/Drivers/chromedriver")

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element(By.ID, "username")

# Enter Your Email Address
username.send_keys("anishmishra4212@gmail.com")

# entering password
pword = driver.find_element(By.ID, "password")

# Enter Your Password
pword.send_keys("Password@1234")	
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Opening Profile
# paste the URL of profile here
profile_url = "https://www.linkedin.com/in/kunalshah1/"

driver.get(profile_url)	 # this will open the link

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
	# this command scrolls the window starting from
	# finalScroll variable
	initialScroll = finalScroll
	finalScroll += 1000

	# we will stop the script for 3 seconds so thatthe data can load
 
	time.sleep(3)
 
	# One can change it as per your needs and internet speed
	end = time.time()

	# scroll for 20 seconds.
	# You can change it as per your needs and internet speed
	if round(end - start) > 20:
		break

src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

print(intro)

name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.get_text().strip()

works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()


location_loc = intro.find_all("span", {'class': 'text-body-small'})

# Ectracting the Location
#location = location_loc[1].get_text().strip()

# Extracting the Location, if available
if len(location_loc) >= 2:
    location = location_loc[1].get_text().strip()
else:
    location = ""

print("Name -->", name,
	"\nWorks At -->", works_at,
	"\nLocation -->", location)
