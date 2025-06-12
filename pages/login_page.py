import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'page_title': 'Protractor practice website - Registration',
        'not_cursor': 'not-allowed',
        'alert_text': 'Username or password is incorrect',
        'success_text': "You're logged in!!",
        'username_label': 'Username',
        'password_label': 'Password',
        'login_button': 'Login'
    }

    def get_field_label(self, locator: tuple) -> str:
        with allure.step(f'Получение текста описания поля'):
            label_locator = (
                locator[0],
                f'{locator[1]}/../label'
            )
            label_text = self.get_text(label_locator)
            return label_text
