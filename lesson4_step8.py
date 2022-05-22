from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим и нажимаем кнопку
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element_by_id("book").click()

    # Находим значение х на странице
    x_num = browser.find_element_by_id("input_value").text

    # Вычисляем значение выражения на странице
    z = calc(x_num)

    # Находим поле для вставки решения и отправляем решение
    pole_answer = browser.find_element_by_id("answer").send_keys(z)

    # Находим и нажимаем кнопку
    button = browser.find_element_by_id("solve").click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла