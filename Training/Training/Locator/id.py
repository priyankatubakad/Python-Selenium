import time

from selenium import webdriver
driver= webdriver.Chrome()

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element(by:'css selectors',value:'input[placeholder="Username"]').click()

