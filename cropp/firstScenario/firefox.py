import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\geckodriver\\win64\\v0.28.0\\geckodriver.exe')
driver.get('https://www.cropp.com/pl/pl/')
driver.maximize_window()
time.sleep(3)
temp = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/input')
temp.send_keys("Koszulka")
time.sleep(5)
temp.send_keys(Keys.ENTER)
time.sleep(7)
temp = driver.find_elements_by_id('categoryProducts')[0].find_elements_by_class_name('es-product')[0]
temp.click()
temp = driver.find_element_by_class_name('sc-gqjmRU')
temp.click()
temp = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/section/div/section[4]/div/div[3]/div/div[2]/div[1]/ul/li[1]').click()