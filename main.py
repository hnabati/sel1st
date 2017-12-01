# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:48:17 2017

@author: hp
"""

from selenium import webdriver
import time
path = "D:\Sel_enium\chromedriver.exe"

driver = webdriver.Chrome(path)

time.sleep(1)
driver.maximize_window()
driver.get("http://www.google.com")

time.sleep(3)

searchbox = driver.find_element_by_name("q")

searchbox.send_keys("Hamid Nabati")
searchbox.submit()
time.sleep(2)

url = driver.current_url
print (url)

title = driver.title
print (title)

links = driver.find_elements_by_class_name ('r')
print (len(links))

print (links[0].text)




driver.quit()


## comment 1