from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Setting up the webdriver
driver = webdriver.Chrome()

#Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)

#Wait for search bar element to be present
wait = WebDriverWait(driver, 10)
search_bar = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

#Searching for the first item
search_bar.send_keys("Bluetooth Speaker")
search_bar.send_keys(Keys.RETURN)

#Waiting for the search results page to load
time.sleep(5)

#Verifying that the search results page has loaded
assert "Bluetooth Speaker" in driver.title

#Selecting a bluetooth speaker from the search results
bluetoothspeaker_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[2]/div[1]/h2/a/span")
bluetoothspeaker_link.click()

#Waiting for the bluetooth speaker details page to load
time.sleep(10)

#Verifying that the correct bluetooth speaker details page has loaded
assert "Bluetooth Speaker" in driver.title

#Adding the bluetooth speaker to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

#Waiting for the cart to update
time.sleep(10)

#Verifying that the bluetooth speaker has been added to the cart
cart_count = driver.find_element("id","nav-cart-count")
assert cart_count.text == "1"

#Searching for the second item
search_bar = driver.find_element("id", "twotabsearchtextbox")
search_bar.send_keys("CY-305R Professional Blender")
search_bar.send_keys(Keys.RETURN)

#Waiting for the search results page to load
time.sleep(5)

#Verifying that the search results page has loaded
assert "CY-305R Professional Blender" in driver.title

#Selecting the CY-305R Professional Blender from the search results
cy305r_blender_link = driver.find_element(By.XPATH, "//span[contains(text(),'CY-305R Professional Blender')]/parent::a")
cy305r_blender_link.click()

#Waiting for the CY-305R Professional Blender details page to load
time.sleep(10)

#Verifying that the correct CY-305R Professional Blender details page has loaded
assert "CY-305R Professional Blender" in driver.title

#Adding the CY-305R Professional Blender to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

#Waiting for the cart to update
time.sleep(10)

#Verifying that both items have been added to the cart
cart_count = driver.find_element("id","nav-cart-count")
assert cart_count.text == "2"

#Closing the webdriver
driver.quit()