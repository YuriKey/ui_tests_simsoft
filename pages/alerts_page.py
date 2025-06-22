import allure

from data.locators.alerts_locators import AlertsLocators as loc
from pages.base_page import BasePage


class AlertsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXT = {
        'name': 'Severus',
        'result_text': 'Hello Severus! How are you today?'
    }

    def press_input_alert(self):
        self.click_element(loc.INPUT_ALERT_BUTTON)

    def trigger_alert(self):
        with allure.step('Вызов алерта'):
            self.switch_to_frame(loc.FRAME_LOCATOR)
            self.click_element(loc.RAISE_ALERT_BUTTON)

    def input_text_and_submit(self):
        with allure.step('Ввод текста и подтверждение алерта'):
            self.switch_to_alert()
            self.fill_alert_input(text=self.EXPECTED_TEXT['name'])
            self.accept_alert()
