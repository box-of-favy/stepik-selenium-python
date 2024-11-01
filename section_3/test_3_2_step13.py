import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=options)  # добавили options

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR,
                                  "div.first_block input.form-control.first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR,
                                  "div.first_block .form-control.second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third").send_keys(
            "test@test.com")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!"

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR,
                                  "div.first_block input.form-control.first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR,
                                  "div.first_block .form-control.second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third").send_keys(
            "test@test.com")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!"

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()


if __name__ == "__main__":
    pytest.main()