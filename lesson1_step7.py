from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # Находим значение х на странице
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    print(x)
    # Вычисляем значение выражения на странице
    y = calc(x)
    # Находим поле для вставки решения
    pole_element = browser.find_element_by_id("answer")
    pole_element.send_keys(y)
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
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла