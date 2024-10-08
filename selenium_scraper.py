from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("http://www.python.org")
time.sleep(5)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
time.sleep(5)
elem.clear()
elem.send_keys("pycon")
time.sleep(5)
elem.send_keys(Keys.RETURN)
time.sleep(25)
assert "No results found." not in driver.page_source
driver.close()
driver.quit()

print('done')