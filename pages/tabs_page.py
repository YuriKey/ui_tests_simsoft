import allure

from data.locators.tabs_locators import TabsLocators as loc
from pages.base_page import BasePage


class TabsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_new_tab(self):
        with allure.step('Открытие новой вкладки'):
            try:
                self.click_element(loc.LINK_NEW_TAB_LOCATOR)
            except Exception as e:
                raise Exception(f'Не удалось открыть новую вкладку: {e}')

    def switch_to_some_tab(self, number: int):
        index = number - 1
        with allure.step(f'Переключение на вкладку {number}'):
            try:
                handles = self.browser.window_handles
                if len(handles) > index >= 0:
                    self.browser.switch_to.window(handles[index])
                else:
                    raise Exception(f'Вкладка с номером {number} не найдена. Всего вкладок: {len(handles)}')
            except Exception as e:
                raise Exception(f'Не удалось переключиться на вкладку {number}: {e}')

    def get_current_tab_index(self) -> int:
        with allure.step('Получение индекса текущей вкладки'):
            try:
                return self.browser.window_handles.index(self.browser.current_window_handle) + 1
            except Exception as e:
                raise Exception(f'Не удалось получить индекс текущей вкладки: {e}')
