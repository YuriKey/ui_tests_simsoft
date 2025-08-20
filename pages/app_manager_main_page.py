import allure
from faker import Faker

from data.locators.manager_page_locators import ManagerPageLocators as loc
from pages.base_page import BasePage


class ManagerPage(BasePage):
    EXPECTED_TEXTS = {
        'page_title': 'Protractor practice website - Banking App',
        'alert_text': 'Customer added successfully with customer id :',
    }

    def __init__(self, browser):
        super().__init__(browser)
        self.fake = Faker()

    def click_manager_login_button(self):
        with allure.step('Нажатие на кнопку "Manager Login"'):
            try:
                self.click_element(loc.MANAGER_LOGIN_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось нажать на кнопку "Manager Login": {e}')

    def click_new_customer_button(self):
        with allure.step('Нажатие на кнопку "Add Customer"'):
            try:
                self.click_element(loc.ADD_CUSTOMER_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось нажать на кнопку "Add Customer": {e}')

    def _generate_user_data(self):
        return {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'postal_code': self.fake.postcode()
        }

    def fill_new_customer_form(self):
        with allure.step('Заполнение формы "Add Customer"'):
            user_data = self._generate_user_data()
            try:
                self.fill_field(loc.FIRST_NAME_FIELD, user_data['first_name'])
                self.fill_field(loc.LAST_NAME_FIELD, user_data['last_name'])
                self.fill_field(loc.POSTAL_CODE_FIELD, user_data['postal_code'])
            except Exception as e:
                raise Exception(f'Не удалось заполнить поля формы "Add Customer": {e}')

    def click_submit_button(self):
        with allure.step('Нажатие на кнопку "Add Customer"'):
            try:
                self.click_element(loc.SUBMIT_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось нажать на кнопку "Submit": {e}')
