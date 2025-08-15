import time

from selenium import webdriver
chrome_driver =webdriver.ChromeOptions()


driver= webdriver.Chrome()

driver.get('https://48.ie/log-in')

driver.find_element('css selector','button[class="btn btn-primary-outline"]').click()
time.sleep(2)
driver.find_element('css selector','input[id="fname"]').send_keys("vivekanandab@gmail.com")
time.sleep(2)
