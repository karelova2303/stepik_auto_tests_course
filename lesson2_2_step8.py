from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открыть линк
    link = "http://suninjuly.github.io/file_input.html"

    # создаём объект WebDriver для браузера chrome
    browser = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element(By.CSS_SELECTOR, "input:nth-child(2)")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input:nth-child(4)")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)")
    input3.send_keys("mail@mail.ru")


    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


