import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.morele.net')
driver.maximize_window()
time.sleep(3)
temp = driver.find_element_by_name('search')
temp.send_keys("Monitor Samsung")
time.sleep(5)
temp.send_keys(Keys.ENTER)
time.sleep(7)
temp = driver.find_elements_by_class_name('cat-list-products')[0].find_element_by_class_name('pushAddToBasketData')
temp.click()


time.sleep(7)
driver.get('https://www.morele.net/kategoria/laptopy-31/')
time.sleep(5)
temp = driver.find_elements_by_class_name('cat-list-products')[0].find_element_by_class_name('pushAddToBasketData')
time.sleep(5)
temp.click()
try:
    temp = WebDriverWait(driver, 5).until(exp.element_to_be_clickable((By.CLASS_NAME, 'js_no-warrant-btn_desktop')))
    temp.click()
    time.sleep(5)
    driver.get('https://www.morele.net/koszyk/')
except TimeoutException:
    driver.get('https://www.morele.net/koszyk/')

temp = driver.find_element_by_xpath('/html/body/div[3]/main/div/div[3]/div/div[1]/div/div[2]/div/ul/li[2]')
driver.execute_script("arguments[0].click();", temp)

try:
    temp = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div[3]/button[2]')
except NoSuchElementException:
    try:
        temp = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[3]/button[2]')
    except NoSuchElementException:
        temp = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div[3]/button[2]')
driver.execute_script("arguments[0].click();", temp)
