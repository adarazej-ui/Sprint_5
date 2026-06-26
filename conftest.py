import pytest
from selenium import webdriver

@pytest.fixture
def my_name():
    return "Анастасия"

@pytest.fixture
def my_email():
    return "anastasiya_ratushnyak48@mail.ru"

@pytest.fixture
def my_password():
    return "123456"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()