from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators

class TestLogout:

    def test_logout_from_personal_account_success(self, driver, my_email, my_password):
        
        driver.get("https://stellarburgers.education-services.ru/login")

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_EMAIL_INPUT))

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(my_email)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(my_password)
        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_BUTTON)).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGOUT_BUTTON)).click()

        # Проверяем успешный возврат на страницу входа
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

