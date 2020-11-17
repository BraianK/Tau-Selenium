import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.morele.net')

temp = driver.find_element_by_name('search')
temp.send_keys("Monitor Samsung")
temp.send_keys(Keys.ENTER)
time.sleep(5)
temp = driver.find_elements_by_class_name('cat-list-products')[0].find_element_by_class_name('pushAddToBasketData')
temp.click()
time.sleep(5)
try:
    temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.CLASS_NAME, 'js_no-warrant-btn_desktop')))
    temp.click()
    time.sleep(5)
    temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.CLASS_NAME, 'show-basket')))
    temp.click()
except TimeoutException:
    driver.get('https://www.morele.net/koszyk/')

# temp.click()
# temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-identity')))
# temp.send_keys("testowyuzytkowniktaubkr")
# temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.ID, 'loginModalForm-password')))
# temp.send_keys("testowyuzytkowniktaubkr123")
# temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.NAME, 'form_submit')))
# temp.click()
# time.sleep(3)
# try:
#     temp = driver.find_elements_by_class_name('listLayout-main')[0].find_elements_by_class_name('threadGrid')[0].find_element_by_class_name('cept-dealBtn')
#
#     temp.click()
# except NoSuchElementException:
#     print('Nie ma możliwości przejścia do okazji')
