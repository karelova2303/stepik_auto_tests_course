from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")
    browser.get(link)

    # находим первое число
    a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    a = int(a_element.text)

    # находим второе число
    b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    b = int(b_element.text)

    # считаем сумму
    sum = str(a + b)

    # ищем совпадение
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(sum)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()