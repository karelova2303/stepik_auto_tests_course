    # Подключаем библиотеки
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Формула для капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"

    # Создаём объект WebDriver для браузера chrome
    browser = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
    button.click()

    # Поиск имени новой вкладки
    new_window = browser.window_handles[1]

    # Переключиться на новую вкладку
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
    # Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Посчитать математическую функцию от x.
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()