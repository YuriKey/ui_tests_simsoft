import json
import os
from typing import List, Dict

import allure


class CookiesHelper:
    def __init__(self, page_object, cookies_file: str):
        self.page = page_object
        self.cookies_file = cookies_file

    @property
    def browser(self):
        return self.page.browser

    def get_cookies(self):
        with allure.step('Получение всех cookies из браузера'):
            cookies = self.browser.get_cookies()
            return cookies

    def add_cookies_to_browser(self, cookies: Dict):
        with allure.step(f'Добавление cookie {cookies} в браузер'):
            self.browser.add_cookie(cookies)

    @staticmethod
    def save_cookies_to_file(cookies: List[Dict], filename: str):
        with allure.step(f'Сохранение cookies в файл {filename}'):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w') as file:
                json.dump(cookies, file, indent=2)

    @staticmethod
    def load_cookies_from_file(filename: str) -> List[Dict]:
        with allure.step(f'Загрузка cookies из файла {filename}'):
            if not os.path.exists(filename):
                raise FileNotFoundError(f'Cookies file {filename} not found')

            with open(filename, 'r') as file:
                return json.load(file)

    def load_cookies_and_refresh(self):
        with allure.step('Загрузка cookies в браузер'):
            cookies = self.load_cookies_from_file(self.cookies_file)
            self.delete_browser_cookies()

            for cookie in cookies:
                self._add_valid_cookie(cookie)

            self.page.refresh_page()

    def _add_valid_cookie(self, cookie: Dict):
        with allure.step(f'валидация и добавление cookies в браузер'):
            required_fields = {'name', 'value', 'domain'}
            if not required_fields.issubset(cookie.keys()):
                raise ValueError(f'В cookies [{cookie}] не найдены обязательные поля: {required_fields}')

            valid_cookie = {
                'name': cookie['name'],
                'value': cookie['value'],
                'domain': cookie['domain'],
                'path': cookie.get('path', '/'),
                'secure': cookie.get('secure', False),
                'httpOnly': cookie.get('httpOnly', False),
                'expiry': cookie.get('expiry')
            }
            valid_cookie = {k: v for k, v in valid_cookie.items() if v is not None}

            try:
                self.add_cookies_to_browser(valid_cookie)
            except Exception as e:
                raise ValueError(f'Не удалось добавить {cookie['name']} в браузер: {e}')

    def delete_browser_cookies(self):
        with allure.step('Удаление cookies в браузере'):
            self.browser.delete_all_cookies()

    def cleanup(self):
        with allure.step('Удаление временного файла cookies'):
            if os.path.exists(self.cookies_file):
                os.remove(self.cookies_file)
