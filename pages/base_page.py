# base_page.py
import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def find_element(self, locator):
        with allure.step(f"Поиск элемента по локатору {locator}"):
            return self.wait.until(EC.visibility_of_element_located(locator))

    def open(self, url):
        with allure.step("Открытие страницы по URL"):
            self.browser.get(url)

    def click_element(self, locator):
        with allure.step(f"Клик по элементу с локатором: {locator}"):
            self.wait.until(
                EC.element_to_be_clickable(locator),
                message=f"Не удалось найти кликабельный элемент с локатором {locator}"
            ).click()

    def click_element_by_js(self, element):
        with allure.step("Клик по элементу с помощью JS"):
            try:
                self.browser.execute_script("""
                    var elem = arguments[0];
                    var event = new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true,
                        view: window
                    });
                    elem.dispatchEvent(event);
                """, element)
            except Exception as e:
                raise Exception(f"Не удалось выполнить JS-клик: {str(e)}")

    def fill_field(self, locator, text):
        with allure.step("Заполнение поля"):
            self.find_element(locator).send_keys(text)

    def element_is_visible(self, locator):
        with allure.step("Проверка видимости элемента"):
            return self.find_element(locator).is_displayed()

    def get_title(self):
        with allure.step("Получение заголовка страницы"):
            return self.browser.title

    def get_current_url(self):
        with allure.step("Получение URL текущей страницы"):
            return self.browser.current_url

    def scroll_to_element(self, locator):
        with allure.step("Скроллинг до элемента"):
            try:
                element = self.find_element(locator)
                self.browser.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});",
                                            element)

            except Exception as e:
                print(f"Ошибка при скроллинге до элемента: {e}")

    def scroll_to_bottom(self):
        with allure.step("Скроллинг до конца страницы"):
            scroll_pause_time = 1
            last_height = self.browser.execute_script("return document.body.scrollHeight")
            while True:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_pause_time)
                new_height = self.browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
