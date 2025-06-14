import allure

from data import urls
from pages.base_page import BasePage
from faker import Faker
from data.locators.login_page_locators import LoginPageLocators as lloc
from data.locators.home_page_locators import HomePageLocators as hloc

url = urls.Urls
fake = Faker()


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'page_title': 'Protractor practice website - Registration',
        'wrong_page_title': 'hello world',
        'not_cursor': 'not-allowed',
        'alert_text': 'Username or password is incorrect',
        'wrong_alert_text': 'Password is incorrect',
        'success_text': "You're logged in!!",
        'username_label': 'Username',
        'password_label': 'Password',
        'login_button': 'Login'
    }

    TEST_CASES = [
        {
            "name": "valid_credentials",
            "credentials": {
                "username": "angular",
                "password": "password",
                "username_desc": f"{fake.word()}"
            },
            "expected": {
                "success": True,
                "url": url.HOME_PAGE,
                "element": hloc.SUCCESS_MESSAGE,
                "text_key": "success_text"
            }
        },
        {
            "name": "invalid_username",
            "credentials": {
                "username": f"{fake.name()}",
                "password": "password",
                "username_desc": f"{fake.word()}",
            },
            "expected": {
                "success": False,
                "url": url.LOGIN_PAGE,
                "element": lloc.ALERT_LOGIN_ERROR,
                "text_key": "alert_text"
            }
        },
        {
            "name": "invalid_password",
            "credentials": {
                "username": "angular",
                "password": f"{fake.password()}",
                "username_desc": f"{fake.word()}"
            },
            "expected": {
                "success": False,
                "url": url.LOGIN_PAGE,
                "element": lloc.ALERT_LOGIN_ERROR,
                "text_key": "alert_text"
            }
        }
    ]

    def get_field_label(self, locator: tuple) -> str:
        with allure.step(f'Получение текста описания поля'):
            label_locator = (
                locator[0],
                f'{locator[1]}/../label'
            )
            label_text = self.get_text_by_locator(label_locator)
            return label_text
