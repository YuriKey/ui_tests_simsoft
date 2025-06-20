import allure
from selenium.webdriver import ActionChains

from data.locators.droppable_locators import DndLocators as loc
from pages.base_page import BasePage


class DndPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'text_before': 'Drop here',
        'text_after': 'Dropped!'
    }

    def switch_to_dnd_frame(self):
        with allure.step('Переключение на фрейм drag and drop'):
            element = self.find_element(loc.FRAME_LOCATOR)
            self.browser.switch_to.frame(element)

    def drag_and_drop(self, draggable: tuple[str, str], droppable: tuple[str, str]) -> None:
        with allure.step('Перетаскивание элемента'):
            try:
                draggable_element = self.find_element(draggable)
                droppable_element = self.find_element(droppable)
                action = ActionChains(self.browser)
                action.drag_and_drop(draggable_element, droppable_element).perform()
            except Exception as e:
                raise Exception(f'Произошла ошибка при перетаскивании: {e}')
