import time

from selenium import webdriver
chrome_driver =webdriver.ChromeOptions()


driver= webdriver.Chrome()

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)
driver.find_element('css selector','a[href="/register"]').click()

driver.find_element('css selector','input[id="gender-female"]').click()
time.sleep(2)
driver.find_element('css selector','input[id="FirstName"]').send_keys("Priya")
time.sleep(2)
driver.find_element('css selector','input[id="LastName"]').send_keys("T")
time.sleep(2)
driver.find_element('css selector','input[name="Email"]').send_keys("priya@gmail.com")
time.sleep(2)
driver.find_element('css selector','input[name="Password"]').send_keys("pudeioe7899@G")
time.sleep(2)
driver.find_element('css selector','input[name="ConfirmPassword"]').send_keys("pudeioe7899@G")
time.sleep(2)
