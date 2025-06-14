import json
import os
from typing import Dict, List

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

    COOKIES_FILE = "sqlex_cookies.json"

    def open_page(self):
        with allure.step('Открытие страницы sqlex.ru'):
            self.browser.get(self.url)
            return self

    @staticmethod
    def save_cookies_to_file(cookies: List[Dict], filename: str = COOKIES_FILE):
        with allure.step('Сохранение cookies в файл'):
            with open(filename, 'w') as file:
                json.dump(cookies, file)

    @staticmethod
    def load_cookies_from_file(filename: str = COOKIES_FILE) -> List[Dict]:
        with allure.step('Загрузка cookies из файла'):
            if not os.path.exists(filename):
                return []

            with open(filename, 'r') as file:
                return json.load(file)

    def sqlex_login(self):
        with allure.step('Авторизация на sql-ex.ru'):
            self.browser.find_element(*loc.LOGIN_FIELD).send_keys(self.credentials['login'])
            self.browser.find_element(*loc.PASSWORD_FIELD).send_keys(self.credentials['password'])
            self.browser.find_element(*loc.SUBMIT_BUTTON).click()
            self.save_cookies_to_file(self.browser.get_cookies())

    def is_logged_in(self) -> bool:
        with allure.step('Проверка авторизации'):
            return self.is_element_clickable(loc.LOGGED_IN_INDICATOR)

    def load_cookies_and_refresh(self):
        with allure.step('Загрузка cookies и обновление страницы'):
            cookies = self.load_cookies_from_file()
            if cookies:
                self.browser.delete_all_cookies()
                for cookie in cookies:
                    self.browser.add_cookie(cookie)
                self.browser.refresh()
