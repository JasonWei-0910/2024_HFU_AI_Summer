from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
for i in range(2000,3000):
    url1 = 'https://cybersec.ithome.com.tw/2024/exhibition-page/'+ str(i)
    driver.get(url1)
    if url1:
        name=driver.find_element(By.CLASS_NAME, 'info-title')
        print('廠商名稱:'+ name.text)
  
        link_elements = driver.find_elements(By.CLASS_NAME, 'border-icon')

        for link_element in link_elements:
            if 'facebook' in link_element.get_attribute('href'):
                print('臉書網址:'+ link_element.get_attribute('href'))
            elif 'twitter' in link_element.get_attribute('href'):
                print('推特網址:'+ link_element.get_attribute('href'))
            elif 'linkedin' in link_element.get_attribute('href'):
                print('linkedin網址:'+ link_element.get_attribute('href'))
            else:
                print('官網網址:'+ link_element.get_attribute('href'))
        print()
    

driver.close()