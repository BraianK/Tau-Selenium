import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Opera(executable_path='C:\\Users\\Braian\\.wdm\\drivers\\operadriver\\win64\\v.86.0.4240.80\\operadriver_win64\\operadriver.exe')

driver.get('https://www.morele.net')

temp = driver.find_element_by_name('search')
temp.send_keys("Monitor Samsung")
temp.send_keys(Keys.ENTER)
time.sleep(5)
driver.maximize_window()
#musiałem dodać maximize window, gdyż w opera nie wyszukuje buttona
temp = driver.find_elements_by_class_name('cat-list-products')[0].find_element_by_class_name('pushAddToBasketData')
time.sleep(5)
temp.click()
time.sleep(5)
try:
    temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.CLASS_NAME, 'js_no-warrant-btn_desktop')))
    temp.click()
    time.sleep(5)
    temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.CLASS_NAME, 'show-basket')))
    temp.click()
    temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.CLASS_NAME, 'confirm-button')))
#czasami w tym fragmencie strona laduje się bardzo długo - wydaje mi się, że jest to kwestia zabezpieczeń, w większości przypadków działa poprawnie
except TimeoutException:
    driver.get('https://www.morele.net/koszyk/')
