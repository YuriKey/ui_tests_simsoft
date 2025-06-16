import os

import allure
from dotenv import load_dotenv

from data.locators.sqlex_locators import SqlexLocators as loc
from pages.base_page import BasePage

load_dotenv()


class SqlexPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://www.sql-ex.ru/'
        self.credentials = {
            'login': os.getenv("LOGIN"),
            'password': os.getenv("PASSWORD")
        }

    def open_page(self):
        with allure.step('Открытие страницы sqlex.ru'):
            self.open(self.url)
            return self

    def sqlex_login(self):
        with allure.step('Авторизация на sql-ex.ru'):
            self.fill_field(loc.LOGIN_FIELD, self.credentials['login'])
            self.fill_field(loc.PASSWORD_FIELD, self.credentials['password'])
            self.click_element(loc.SUBMIT_BUTTON)

    def is_logged_in(self) -> bool:
        with allure.step('Проверка авторизации'):
            return self.is_element_clickable(loc.LOGGED_IN_INDICATOR)
