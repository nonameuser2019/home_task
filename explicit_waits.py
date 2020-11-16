from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
driver.get(url)
# поиск элемента с ценой на сайте, и ожидание пока цена не станет 100
price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
# как только цена стала 100 находим кнопку, проверяем что она активна, и совершаем клик
book_button = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.ID, 'book')))
book_button.click()
input_val = driver.find_element_by_id('input_value').text

answer = driver.find_element_by_id('answer')
answer.send_keys(calc(int(input_val)))

submit_button = WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.ID, 'solve')))
submit_button.click()
