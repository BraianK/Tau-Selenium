from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
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

temp = driver.find_element_by_class_name('test-loginButton')

temp.click()
logger.info('Wpisuję poświadczenia')
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-identity')))
temp.send_keys("testowyuzytkowniktaubkr")
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-password')))
temp.send_keys("testowyuzytkowniktaubkr123")
logger.info('Loguję się')
temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.NAME, 'form_submit')))
temp.click()
logger.info('Zalogowano')
driver.close()