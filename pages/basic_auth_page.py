import os

import allure
import easyocr
import pyautogui
from dotenv import load_dotenv

from data.locators.basic_auth_locators import BasicAuthLocators as loc
from pages.base_page import BasePage

load_dotenv()


class BasicAuthPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_display_image(self):
        with allure.step('Нажатие кнопки "Display Image"'):
            try:
                self.click_element(loc.DISPLAY_IMAGE_LOCATOR)
                self.await_for_js_reaction()
            except Exception as e:
                raise Exception(f'Ошибка при нажатии кнопки "Display Image": {str(e)}')

    def fill_fields_and_accept(self):
        with allure.step('Заполнение полей и нажатие кнопки "OK"'):
            try:
                pyautogui.write(os.getenv('WATCH_LOGIN'))
                self.await_for_js_reaction()
                pyautogui.press('tab')
                pyautogui.write(os.getenv('WATCH_PASSWORD'))
                pyautogui.press('enter')
            except Exception as e:
                raise Exception(f'Ошибка при заполнении полей окна авторизации: {str(e)}')

    def is_image_displayed(self):
        with allure.step('Проверка отображения картинки с учетными данными'):
            try:
                return self.is_element_visible(loc.AUTH_IMAGE)
            except Exception as e:
                raise Exception(f'Изображение не отображается: {str(e)}')

    def get_credentials_from_image(self):
        with allure.step('Получение текста из изображения'):
            try:
                auth_image = self.find_element(loc.AUTH_IMAGE)
                img_bytes = auth_image.screenshot_as_png

                reader = easyocr.Reader(['en'])
                result = reader.readtext(img_bytes, detail=0)
                credentials = self.parse_credentials(" ".join(result))
                return credentials

            except Exception as e:
                raise Exception(f'Ошибка при получении данных из изображения: {str(e)}')

    @staticmethod
    def parse_credentials(text):
        with allure.step('Парсинг текста изображения'):
            try:
                clean_text = text.replace("HTTP Basic Authentication:", "").strip()

                parts = clean_text.split()

                credentials = {
                    'username': parts[1] if len(parts) > 1 else None,
                    'password': parts[3] if len(parts) > 3 else None
                }

                return credentials

            except Exception as e:
                raise Exception(f"Ошибка при парсинге: {str(e)}")
