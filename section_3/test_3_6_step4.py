from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestMainPage():
    def setup_method(self):
        self.link = "https://stepik.org/lesson/236895/step/1"

    def test_login(self, browser, config):
        username = config['credentials']['username']
        password = config['credentials']['password']

        browser.get(self.link)
        login_button = browser.find_element(By.CSS_SELECTOR, "a[href*='auth=login']")
        login_button.click()

        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys(username)
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys(password)
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, "login_form")))