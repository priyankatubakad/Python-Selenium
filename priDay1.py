import time

from selenium import webdriver

from Training.Locator.action_chain import action_chain_obj

chrome_driver = webdriver.ChromeOptions()
import selenium.webdriver.common.action_chains

driver = webdriver.Chrome()

driver.get("https://48.ie/log-in")
time.sleep(2)
driver.maximize_window()
time.sleep(1)

driver.find_element('css selector', 'input[id="email"]').send_keys("priyanka_tubakad@thbs.com")
time.sleep(1)
driver.find_element('css selector', 'input[id="pwd-type"]').send_keys("thbs123!")
time.sleep(1)
driver.find_element("xpath", '/html/body/app-root/div/div/div[2]/div/app-login/div/form/div[5]/div[1]/button').click()
time.sleep(1)
ref_ele=driver.find_element("xpath", '//*[@id="navbarDropdown1"]').click()
action_chain_obj.move_to_element(ref_ele).perform()
time.sleep(3)
driver.find_element("xpath", '//*[@id="navbarDropdown2"]').click()
time.sleep(3)
driver.find_element("xpath", '//*[@id="navbarDropdown3"]').click()
time.sleep(3)
driver.find_element("xpath", '//*[@id="navbarDropdown4"]').click()
time.sleep(3)
driver.close()
