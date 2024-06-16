from modulefinder import Module

import button as button
import select
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


# Initialize the WebDriver
driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()

# Navigate to the URL
driver.get("https://automationplayground.com/crm/login.html")
time.sleep(4)
# Input Credentials
driver.find_element(By.NAME, "email-name").send_keys("123qwe@gmail.com")
time.sleep(2)
driver.find_element(By.NAME, "password-name").send_keys("123qwe")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[3]/label/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/button").click()
time.sleep(3)


# Search...........................
driver.find_element(By.XPATH, "/html/body/nav/input").send_keys("Manual Testing")
time.sleep(4)
# Edit Icon
driver.find_element(By.CLASS_NAME, "icon-pencil").click()
time.sleep(5)
# Back_to_Customer
driver.find_element(By.XPATH, "/html/body/div/div/div[7]/div[2]/a").click()
time.sleep(8)

# New_Customer
driver.find_element(By.XPATH, "/html/body/div/a").click()
time.sleep(3)

# Email
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[1]/input").send_keys("14qwe@gmail.com")
time.sleep(3)
# First Name
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[2]/input").send_keys("John Doe")
time.sleep(3)
# Last Name
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[3]/input").send_keys("Doe")
time.sleep(3)
# City
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[4]/input").send_keys("India")
time.sleep(3)
# State
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/select").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/select").send_keys("Alabama")
time.sleep(3)
# Gender
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[6]/input[1]").click()
time.sleep(3)
#  Add to promotional list
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[7]/input").click()
time.sleep(3)
# Sumit Button
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
time.sleep(5)
# Cancel Button
driver.find_element(By.CSS_SELECTOR, 'a').click()
time.sleep(5)

# # Customer Service
driver.find_element(By.LINK_TEXT, "Customer Service").click()
time.sleep(5)
# # SignOut
driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(10)

driver.quit()

