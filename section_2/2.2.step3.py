from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

try:
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    print(x)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    print(y)

    def calc(x,y):
        return str(int(x) + int(y))

    z = calc(x,y)
    print(z)

    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_value(z)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
