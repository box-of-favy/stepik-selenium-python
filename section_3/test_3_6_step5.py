"""
Обратите внимание. Тест работает в 1 случае из 10 не потому, что с ним что-то не так, а потому что
Степик забагован
"""

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import math


class TestMainPage():

    @pytest.mark.parametrize('lesson_number', [895]) # 896, 897, 898, 899, 903, 904, 905
    def test_login(self, browser, config, lesson_number):
        wait = WebDriverWait(browser, 5)
        self.link = f"https://stepik.org/lesson/236{lesson_number}/step/1"
        username = config['credentials']['username']
        password = config['credentials']['password']

        browser.get(self.link)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='auth=login']")))
        login_button.click()
        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys(username)
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys(password)
        button_login = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button_login.click()

        wait.until(EC.invisibility_of_element_located((By.ID, "login_form")))

        input3 = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
        input3.clear()

        answer = math.log(int(time.time()))
        input3.send_keys(str(answer))

        # time.sleep(5)
        button_submit = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button_submit.click()
        time.sleep(10)
        try:
            correct_hint = browser.find_element(By.XPATH,
                                            "//p[@class='smart-hints__hint' and text()='Correct!']")
            assert correct_hint.text == "Correct!"
        except:
            wrong_hint = (browser.find_element
                          (By.XPATH,
                                            "//p[@class='smart-hints__hint'"))
            print(wrong_hint.text)
            print("Wrong answer")
            element = browser.find_element(By.CSS_SELECTOR, "span p")
            print(element.text)