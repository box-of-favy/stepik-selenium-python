from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

try:
    x = browser.find_element(By.CSS_SELECTOR, "span.nowrap#input_value").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
