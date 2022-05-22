from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим и нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn").click()
    
    # Находим названия вкладок: новой и старой
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    # Переходим на новую вкладку
    browser.switch_to.window(new_window)

    # Находим значение х на странице
    x_num = browser.find_element_by_id("input_value").text

    # Вычисляем значение выражения на странице
    z = calc(x_num)

    # Находим поле для вставки решения и отправляем решение
    pole_answer = browser.find_element_by_id("answer").send_keys(z)

    # Находим и нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла