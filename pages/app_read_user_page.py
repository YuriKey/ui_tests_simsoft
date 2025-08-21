import random

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from data.locators.read_user_page_locators import ReadUserPageLocators as loc
from pages.base_page import BasePage


class ReadUserPage(BasePage):
    EXPECTED_TEXTS = {
        'alert_text': 'Account created successfully with account Number :'
    }

    def __init__(self, browser):
        super().__init__(browser)

    def fill_customer_name(self, name='Test'):
        with allure.step(f'Заполнение поля "Customer Name" значением "{name}"'):
            try:
                self.click_element(loc.USER_SELECT)
                option_locator = (By.XPATH, f"//option[contains(text(), '{name}')]")
                self.click_element(option_locator)
            except Exception as e:
                raise Exception(f'Не удалось заполнить поле "Customer Name". Ошибка: {e}')

    def fill_currency(self):
        with allure.step("Выбираем случайную валюту"):
            try:
                select = Select(self.find_element(loc.CURRENCY_SELECT))

                all_options = select.options[1:]

                if not all_options:
                    raise Exception("Нет доступных вариантов валют")

                random_option = random.choice(all_options)
                currency_value = random_option.get_attribute('value')
                currency_text = random_option.text.strip()

                select.select_by_value(currency_value)

                return currency_text

            except Exception as e:
                raise Exception(f"Не удалось выбрать валюту: {e}")

    def process_button_click(self):
        with allure.step('Нажатие на кнопку "Process"'):
            try:
                self.click_element(loc.PROCESS_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось нажать на кнопку "Process"')
