import time

from selenium import webdriver
chrome_driver =webdriver.ChromeOptions()


driver= webdriver.Chrome()

driver.get('https://demowebshop.tricentis.com/')

driver.find_element('css selector','button[class="btn btn-primary-outline"]').click()
time.sleep(2)
