import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

logger = logging.getLogger('TAU')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Firefox(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\geckodriver\\win64\\v0.28.0\\geckodriver.exe')
logger.info('Przechodzę na stronę CROPP')
driver.get('https://www.cropp.com/pl/pl/')
logger.info('Maksymalizuję przeglądarkę')
driver.maximize_window()
temp = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/button[2]').click()
time.sleep(5)
logger.info('Loguję się')
temp = driver.find_element_by_id('login[username]_id')
temp.send_keys("ldy02073@eoopy.com")
temp = driver.find_element_by_id('login[password]_id')
temp.send_keys("testtau123")
temp = driver.find_element_by_class_name('sc-gqjmRU').click()
time.sleep(3)
logger.info('Zalogowano')
logger.info('Wyszukuję koszulki')
temp = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/input')
temp.send_keys("Koszulka")
time.sleep(5)
temp.send_keys(Keys.ENTER)
time.sleep(7)
logger.info('Dodaję przedmiot do koszyka')
temp = driver.find_elements_by_id('categoryProducts')[0].find_elements_by_class_name('es-product')[0]
temp.click()
temp = driver.find_element_by_class_name('sc-gqjmRU')
temp.click()
temp = driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/section/div/section[4]/div/div[3]/div/div[2]/div[1]/ul/li[1]').click()





