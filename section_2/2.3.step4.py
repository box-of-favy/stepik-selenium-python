from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

link = "https://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()