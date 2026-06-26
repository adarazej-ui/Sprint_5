import random
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import random
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators

class TestRegistration:

    def test_registration_success(self, driver, my_name, my_password):
        
        driver.get("https://stellarburgers.education-services.ru/register")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(StellarBurgersLocators.REG_NAME_INPUT))

        unique_email = f"anastasiya_ratushnyak48+{random.randint(10000, 99999)}@mail.ru"

        driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT).send_keys(my_name)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT).send_keys(my_password)

        submit_btn = driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON)
        
        ActionChains(driver).scroll_to_element(submit_btn).perform()
        
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_SUBMIT_BUTTON))
        submit_btn.click()

        WebDriverWait(driver, 7).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_registration_invalid_password_error(self, driver, my_name, my_email):
    
        driver.get("https://stellarburgers.education-services.ru/register")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(StellarBurgersLocators.REG_NAME_INPUT))

        driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT).send_keys(my_name)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT).send_keys(my_email)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT).send_keys("12345") # Пароль 5 знаков

        submit_btn = driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON)
        ActionChains(driver).scroll_to_element(submit_btn).perform()
        
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_SUBMIT_BUTTON))
        submit_btn.click()

        error_msg = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(StellarBurgersLocators.REG_INVALID_PASSWORD_ERROR)
        )
        assert error_msg.is_displayed()