import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.cropp.com/pl/pl/')
driver.maximize_window()
temp = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/button[2]').click()
time.sleep(5)
temp = driver.find_element_by_id('login[username]_id')
temp.send_keys("ldy02073@eoopy.com")
temp = driver.find_element_by_id('login[password]_id')
temp.send_keys("testtau123")
temp = driver.find_element_by_class_name('sc-gqjmRU').click()