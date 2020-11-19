from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
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

temp = driver.find_element_by_class_name('test-loginButton')

temp.click()
logger.info('Wpisuję poświadczenia')
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-identity')))
temp.send_keys("testowyuzytkowniktaubkr")
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-password')))
temp.send_keys("testowyuzytkowniktaubkr123")
logger.info('Loguję się')
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.NAME, 'form_submit')))
logger.info('Zalogowano')
temp.click()
