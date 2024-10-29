from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()

link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'somefile.txt')
try:
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("email@example.com")
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

