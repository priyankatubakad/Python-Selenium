import time

from selenium import webdriver
chrome_driver =webdriver.ChromeOptions()
driver= webdriver.Chrome()
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opts)
from selenium.webdriver.common.action_chains import ActionChains
action_chain_obj = ActionChains(driver)

driver.get('https://www.flipkart.com/')
time.sleep(6)
ele = driver.find_element('xpath','//div[@aria-label="Electronics"]')
action_chain
time.sleep(2)


##functions, generators and decorators - python concepts read