from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # Находим значение х на странице
    x_num = browser.find_element_by_id("input_value").text

    # Вычисляем значение выражения на странице
    z = calc(x_num)

    # Находим поле для вставки решения
    pole_answer = browser.find_element_by_id("answer")
   
    # Проматываем страницу вниз
    browser.execute_script("return arguments[0].scrollIntoView(true);", pole_answer)

    # Вводим ответ в текстовое поле
    pole_answer.send_keys(z)

    # Находим чекбокс
    chkbox_element = browser.find_element_by_id("robotCheckbox")
    chkbox_element.click()
    
    # находим радиокнопку роботы рулят
    robo_element = browser.find_element_by_id("robotsRule")
    robo_element.click()

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