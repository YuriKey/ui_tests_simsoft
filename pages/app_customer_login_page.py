from selenium.webdriver.support.select import Select

from data.locators.customer_login_page_locators import CustomerPageLocators as loc
from pages.base_page import BasePage


class CustomerLoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def customer_select(self, customer_name) -> None:
        try:
            select = Select(self.find_element(loc.CUSTOMER_SELECT))
            select.select_by_visible_text(customer_name)
        except Exception as e:
            raise Exception(f"Не удалось заполнить поле 'Your Name': {e}")

    def click_login_button(self) -> None:
        try:
            self.click_element(loc.LOGIN_BUTTON)
        except Exception as e:
            raise Exception(f"Не удалось кликнуть на кнопку 'Login': {e}")
