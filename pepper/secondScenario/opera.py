import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging

logger = logging.getLogger('TAU')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


driver = webdriver.Opera(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\operadriver\\win64\\v.86.0.4240.80\\operadriver_win64\\operadriver.exe')
logger.info('Przechodzę na stronę pepper')
driver.get('https://www.pepper.pl/')
time.sleep(3)
try:
    logger.info('Przechodzę do okazji')
    temp = driver.find_elements_by_class_name('listLayout-main')[0].find_elements_by_class_name('threadGrid')[0].find_element_by_class_name('cept-dealBtn')
    temp.click()
except NoSuchElementException:
    logger.error('Nie można było przejść do okazji')
    print('Nie ma możliwości przejścia do okazji')
