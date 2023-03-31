from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Setting up the webdriver
driver = webdriver.Chrome()

#Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
driver.maximize_window()

#Wait for search bar element to be present
wait = WebDriverWait(driver, 10)
search_bar = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

#Searching for the first item
search_bar.send_keys("Bluetooth Speaker")
search_bar.send_keys(Keys.RETURN)

#Wait for search results to load and verify the page title
wait.until(EC.title_contains("Bluetooth Speaker"))

#Selecting a bluetooth speaker from the search results
bluetoothspeaker_link = driver.find_element(By.XPATH, "//span[contains(text(),'Bluetooth Speaker')]/ancestor::a")
bluetoothspeaker_link.click()

#Wait for the bluetooth speaker details page to load and verify the page title
wait.until(EC.title_contains("Bluetooth Speaker"))

#Adding the bluetooth speaker to the cart
try:
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
    add_to_cart_button.click()
    #Wait for the cart to update and verify that the item has been added
    wait.until(EC.text_to_be_present_in_element((By.ID, "nav-cart-count"), "1"))
except:
    print("Failed to add Bluetooth Speaker to cart")

#Go back to the homepage
driver.get("https://www.amazon.ca")

#Wait for search bar element to be present
search_bar = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

#Searching for the second item
search_bar.send_keys("CY-305R Professional Blender")
search_bar.send_keys(Keys.RETURN)

#Wait for search results to load and verify the page title
wait.until(EC.title_contains("CY-305R Professional Blender"))

#Selecting the CY-305R Professional Blender from the search results
cy305r_blender_link = driver.find_element(By.XPATH, "//span[contains(text(),'CY-305R Professional Blender')]/ancestor::a")
cy305r_blender_link.click()

#Wait for the CY-305R Professional Blender details page to load and verify the page title
wait.until(EC.title_contains("CY-305R Professional Blender"))

#Adding the CY-305R Professional Blender to the cart
try:
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button")
    add_to_cart_button.click()
    #Wait for the cart to update and verify that both items have been added
    wait.until(EC.text_to_be_present_in_element((By.ID, "nav-cart-count"), "2"))
except:
    print("Failed to add CY-305R Professional Blender to cart")

#Closing the webdriver
driver.quit()

