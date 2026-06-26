import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators

class TestLogin:

    @pytest.mark.parametrize(
        "page_path, click_locator",
        [
            ("", StellarBurgersLocators.MAIN_LOGIN_BUTTON),
            ("", StellarBurgersLocators.ACCOUNT_BUTTON),
            ("register", StellarBurgersLocators.REG_LOGIN_LINK),
            ("forgot-password", StellarBurgersLocators.FORGOT_LOGIN_LINK)
        ]
    )
    def test_login_from_different_entry_points(self, driver, page_path, click_locator, my_email, my_password):
        base_url = "https://stellarburgers.education-services.ru/"
        driver.get(f"{base_url}{page_path}")

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(click_locator)).click()

        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_EMAIL_INPUT))

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(my_email)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(my_password)
        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(base_url))
        assert driver.current_url == base_url