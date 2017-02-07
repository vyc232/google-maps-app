#! /usr/bin/python

import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www.google.com/maps")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchboxinput"))
    )
except TimeoutException:
	print("waited too long")

print(sys.argv)
input = ""
for i in sys.argv[1:]:
	input += i + " "

# Search of the location
searchboxinput = driver.find_element_by_id("searchboxinput")
searchboxinput.send_keys(input)
driver.find_element_by_id("searchbox-searchbutton").click()

# driver.quit()


