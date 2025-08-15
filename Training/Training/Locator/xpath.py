##
##import time
##from selenium import webdriver
##opts = webdriver.ChromeOptions()
##opts.add_experimental_option("detach",True)

##driver = webdriver.Chrome(options=opts)

##driver.get(r"C:/Users/vivek/Downloads/demo.html")
##time.sleep(2)
##driver.find_element('xpath','//td[text()="C#"]/..//input[@type="checkbox"]').click()
##

##second example for dependent and independent and indexing

import time
from selenium import
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.moneycontrol.com/")
time.sleep(6)
driver.find_element('xpath', '//input[@id="search_str"]').click()
time.sleep(6)
driver.find_element('xpath', '//input[@id="search_str"]').send_keys('tata')
time.sleep(4)
driver.find_element('xpath', '(//a[@class="top_search_btn"])[1]').click()
time.sleep(3)




