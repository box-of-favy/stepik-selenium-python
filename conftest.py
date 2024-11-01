import pytest
import yaml
import os
from selenium import webdriver

@pytest.fixture(scope="session")
def config():
    """Загружает конфигурацию из файла config.yaml"""
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="function")
def browser(config):
    """Создает экземпляр браузера Selenium"""
    print("\nstart browser for test..")
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    yield driver
    print("\nquit browser..")
    driver.quit()