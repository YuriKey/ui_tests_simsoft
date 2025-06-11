from data.urls import Urls
from pages.base_page import BasePage

url = Urls()


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'page_title': 'Protractor practice website - Registration',
        'not_cursor': 'not-allowed',
        'alert_text': 'Username or password is incorrect',
        'success_text': "You're logged in!!"
    }
