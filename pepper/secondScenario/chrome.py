import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.pepper.pl/')

time.sleep(3)
try:
    temp = driver.find_elements_by_class_name('listLayout-main')[0].find_elements_by_class_name('threadGrid')[0].find_element_by_class_name('cept-dealBtn')
    temp.click()
except NoSuchElementException:
    print('Nie ma możliwości przejścia do okazji')
