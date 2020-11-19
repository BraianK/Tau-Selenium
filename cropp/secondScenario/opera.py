import time

from selenium import webdriver
import logging

logger = logging.getLogger('TAU')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Opera(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\operadriver\\win64\\v.86.0.4240.80\\operadriver_win64\\operadriver.exe')
logger.info('Przechodzę na stronę CROPP')
driver.get('https://www.cropp.com/pl/pl/')
logger.info('Maksymalizuję przeglądarkę')
driver.maximize_window()
logger.info('Loguję się')
temp = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/button[2]').click()
time.sleep(5)
temp = driver.find_element_by_id('login[username]_id')
temp.send_keys("ldy02073@eoopy.com")
temp = driver.find_element_by_id('login[password]_id')
temp.send_keys("testtau123")
temp = driver.find_element_by_class_name('sc-gqjmRU').click()
logger.info('Zalogowano')