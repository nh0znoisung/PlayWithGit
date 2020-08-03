import time
from selenium import webdriver

#Username
user = "tuanbo2001@gmail.com"




driver = webdriver.Chrome()
driver.get('https://mail.google.com/')

elem = driver.find_element_by_id("identifierId")
elem.send_keys(user)

# driver.find_element_by_xpath("")

driver.back()
driver.forward()


# sarchbox = driver.find_element_by_xpath('//*[@id="search"]')



