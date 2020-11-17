import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\geckodriver\\win64\\v0.28.0\\geckodriver.exe')

driver.get('https://www.pepper.pl/')

time.sleep(3)
try:
    temp = driver.find_elements_by_class_name('listLayout-main')[0].find_elements_by_class_name('threadGrid')[
        0].find_element_by_class_name('cept-dealBtn')
    temp.click()
except NoSuchElementException:
    print('Nie ma możliwości przejścia do okazji')
