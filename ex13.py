from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


# Формула для капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Посчитать математическую функцию от x.
    y = calc(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()