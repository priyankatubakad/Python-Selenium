import time
## Launching the chrome browser
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver= webdriver.Chrome(opts)

#to launch web application
driver.get('https://www.myntra.com')
time.sleep(2)

driver.maximize_window()
time.sleep(2)

#driver.minimize_window()
#time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

print(driver.name)
print(driver.current_url)
print(driver.title)
driver.close()


