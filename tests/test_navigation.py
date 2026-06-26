import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators

class TestNavigation:

    def test_navigate_to_personal_account_page(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    @pytest.mark.parametrize(
        "target_locator",
        [
            StellarBurgersLocators.CONSTRUCTOR_BUTTON,
            StellarBurgersLocators.LOGO_BUTTON
        ]
    )
    def test_navigate_from_login_to_constructor(self, driver, target_locator):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*target_locator).click()
        
        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"