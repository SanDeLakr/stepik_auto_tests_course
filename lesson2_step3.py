from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # Находим значение х на странице
    num1 = browser.find_element_by_id("num1").get_attribute('innerHTML')
    num2 = browser.find_element_by_id("num2").get_attribute('innerHTML')
    # Вычисляем значение выражения на странице
    z = str(int(num1) + int(num2))
    # Находим поле для вставки решения
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла