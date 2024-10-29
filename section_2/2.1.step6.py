from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

link = "https://suninjuly.github.io/math.html"
browser.get(link)

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "span.nowrap#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, 'input.form-check-input[type="checkbox"]')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
