import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Opera(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\operadriver\\win64\\v.86.0.4240.80\\operadriver_win64\\operadriver.exe')

driver.get('https://www.pepper.pl/')
time.sleep(3)
try:
    temp = driver.find_elements_by_class_name('listLayout-main')[0].find_elements_by_class_name('threadGrid')[0].find_element_by_class_name('cept-dealBtn')
    temp.click()
except NoSuchElementException:
    print('Nie ma możliwości przejścia do okazji')
