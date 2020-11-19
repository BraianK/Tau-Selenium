import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import logging

logger = logging.getLogger('TAU')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome(ChromeDriverManager().install())

logger.info('Przechodzę na stronę pepper')
driver.get('https://www.pepper.pl/')
logger.info('Loguję się:')
temp = driver.find_element_by_class_name('test-loginButton')

temp.click()
logger.info('Wpisuję poświadczenia')
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-identity')))
temp.send_keys("testowyuzytkowniktaubkr")
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-password')))
temp.send_keys("testowyuzytkowniktaubkr123")
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.NAME, 'form_submit')))
temp.click()
time.sleep(3)
try:
    logger.info('Przechodzę do okazji')
    temp = driver.find_elements_by_class_name('listLayout-main')[0].find_elements_by_class_name('threadGrid')[0].find_element_by_class_name('cept-dealBtn')

    temp.click()
except NoSuchElementException:
    logger.error('Nie można przejść do okazji')
    print('Nie ma możliwości przejścia do okazji')
