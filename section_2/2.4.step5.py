from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("https://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text