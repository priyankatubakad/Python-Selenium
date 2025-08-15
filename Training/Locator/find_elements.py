import time

from selenium import webdriver
chrome_driver =webdriver.ChromeOptions()
driver= webdriver.Chrome()
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(options=opts)

driver.get('https://www.goibibo.com/')
time.sleep(6)
driver.find_element('xpath','//span[text()="Departure"]').click()
time.sleep(2)

while True:
    month = driver.find_element('xpath','//div[@class="DayPicker-Caption"]')
    print(month.text)


    if month.text == 'January 2025':
        driver.find_element('xpath','//div[@aria-label="Wed Jan 01 2025"]').click()
        break
        # print(month.text)
    else:
        driver.find_element('xpath','//span[@aria-label="Next Month"]').click()
