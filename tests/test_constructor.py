import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators

class TestConstructor:

    @pytest.mark.parametrize(
        "tab_locator, expected_tab_name",
        [
            (StellarBurgersLocators.TAB_SAUCES, "Соусы"),
            (StellarBurgersLocators.TAB_FILLINGS, "Начинки"),
            (StellarBurgersLocators.TAB_BUNS, "Булки")
        ]
    )
    def test_constructor_tab_switching(self, driver, tab_locator, expected_tab_name):
        driver.get("https://stellarburgers.education-services.ru/")
        
        if expected_tab_name == "Булки":
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_SAUCES)).click()
            WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(StellarBurgersLocators.ACTIVE_TAB, "Соусы"))

        tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tab_locator))
        tab.click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(StellarBurgersLocators.ACTIVE_TAB, expected_tab_name))
        
        active_tab_element = driver.find_element(*StellarBurgersLocators.ACTIVE_TAB)
        assert expected_tab_name in active_tab_element.text