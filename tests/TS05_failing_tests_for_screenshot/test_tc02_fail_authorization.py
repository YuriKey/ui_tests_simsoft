import allure
from faker import Faker

from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls
from utils.decorators import screenshot_on_failure

urls = Urls()
fake = Faker()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Авторизация с невалидным паролем')
@allure.severity(allure.severity_level.NORMAL)
@screenshot_on_failure
def test_login_with_invalid_data(open_auth_page):
    auth_page = open_auth_page
    exp_text = auth_page.EXPECTED_TEXTS

    with allure.step('1. Заполнить поля ввода значениями "angula" и "password"'):
        auth_page.fill_field(loc.USERNAME_FIELD, 'angula'), \
            'Не удалось ввести в поле "Username" значение "angula"'
        auth_page.fill_field(loc.PASSWORD_FIELD, 'password'), \
            'Не удалось ввести в поле "Password" значение "password"'
        auth_page.fill_field(loc.USERNAME_DESC_FIELD, f'{fake.lexify(text='????####')}'), \
            'Не удалось заполнить поле "Username *"'

    with allure.step('2. Нажать кнопку "Login". Проверить текст сообщения об ошибке'):
        auth_page.click_element(loc.LOGIN_BUTTON), \
            'Не удалось нажать кнопку "Login"'
        alert = auth_page.find_element(loc.ALERT_LOGIN_ERROR)

        assert auth_page.get_text(alert) == exp_text['wrong_alert_text'], 'Текст сообщения об ошибке не совпадает'
