import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.locators.customers_list_locators import CustomersListLocators as loc
from pages.base_page import BasePage


class CustomersListPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def fill_search_field(self, search_text='Test'):
        with allure.step('Заполнение поля поиска значением "Test"'):
            try:
                self.fill_field(loc.SEARCH_INPUT, search_text)
            except Exception as e:
                raise Exception(f'Не удалось заполнить поле поиска. Ошибка: {e}')

    def clean_search_field(self):
        try:
            element = self.find_element(loc.SEARCH_INPUT)
            element.clear()
        except Exception as e:
            raise Exception(f'Не удалось очистить поле поиска. Ошибка: {e}')

    def delete_button_click(self):
        with allure.step('Нажатие на кнопку "Удалить"'):
            try:
                self.click_element(loc.DELETE_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось нажать на кнопку "Удалить". Ошибка: {e}')

    def get_name_list(self):
        wait = WebDriverWait(self.browser, 10)
        table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

        rows = table.find_elements(By.TAG_NAME, "tr")[1:]

        column_index = 0
        column_data = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > column_index:
                column_data.append(cells[column_index].text.strip())

        return column_data
