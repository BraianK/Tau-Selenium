import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\geckodriver\\win64\\v0.28.0\\geckodriver.exe')

driver.get('https://www.pepper.pl/')

temp = driver.find_element_by_class_name('test-loginButton')

temp.click()
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-identity')))
temp.send_keys("testowyuzytkowniktaubkr")
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-password')))
temp.send_keys("testowyuzytkowniktaubkr123")
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.NAME, 'form_submit')))
temp.click()
time.sleep(3)
try:
    temp = driver.find_elements_by_class_name('listLayout-main')[0].find_elements_by_class_name('threadGrid')[
        0].find_element_by_class_name('cept-dealBtn')
    # temp = driver.find_elements_by_class_name('listLayout-main')[0].find_element_by_class_name('cept-dealBtn')
    #
    temp.click()
except NoSuchElementException:
    print('Nie ma możliwości przejścia do okazji')
