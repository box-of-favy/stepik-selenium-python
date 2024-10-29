from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

# Можно выбрать любую ссылку, для проверки работы скрипта, как на первом сайте регистрации,
# так и на втором
# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third")
    input3.send_keys("Smolensk")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()