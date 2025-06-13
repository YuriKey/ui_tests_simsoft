import allure
import pytest
from faker import Faker

from data.locators.login_page_locators import LoginPageLocators as lloc
from data.locators.home_page_locators import HomePageLocators as hloc
from data.urls import Urls

urls = Urls()
fake = Faker()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Авторизация all type data')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    'name, username, password, username_desc',
    [
        ('Валидные данные', 'angular', 'password', f'{fake.word()}'),
        ('Невалидный username', f'{fake.name()}', 'password', f'{fake.word()}'),
        ('Невалидный password', 'angular', f'{fake.password()}', f'{fake.word()}')
    ],
    ids=['valid_data', 'invalid_username', 'invalid_password']
)
def test_login_authorization(open_auth_page, pages, name, username, password, username_desc):
    auth_page = open_auth_page
    home_page = pages.home
    exp_text = auth_page.EXPECTED_TEXTS

    with allure.step(f'Тестовый случай: {name}'):
        with allure.step('1. Заполнить поля формы'):
            auth_page.fill_field(lloc.USERNAME_FIELD, username)
            auth_page.fill_field(lloc.PASSWORD_FIELD, password)
            auth_page.fill_field(lloc.USERNAME_DESC_FIELD, username_desc)

        with allure.step('2. Нажать  кнопку "Login"'):
            auth_page.click_element(lloc.LOGIN_BUTTON)

        if name == 'Валидные данные':
            home_page.await_for_js_reaction()
            with allure.step('3. Проверка URL страницы'):
                assert home_page.get_current_url() == urls.HOME_PAGE, \
                    'URL страницы не соответствует ожидаемому'
            with allure.step('4. Проверка заголовка страницы'):
                assert home_page.get_title() == exp_text['page_title'], \
                    'Заголовок страницы не соответствует ожидаемому'
            with allure.step('5. Проверка текста сообщения'):
                assert home_page.get_text_by_locator(hloc.SUCCESS_MESSAGE) == \
                        exp_text['success_text'], \
                        'Текст сообщения не соответствует ожидаемому'
        else:
            with allure.step('3. Проверка URL страницы'):
                assert auth_page.get_current_url() != urls.HOME_PAGE, \
                    'URL страницы изменился'
            with allure.step('4. Проверка наличия сообщения'):
                assert auth_page.is_element_visible(lloc.ALERT_LOGIN_ERROR), \
                    'Не отображается сообщение об ошибке'
            with allure.step('5. Проверка текста сообщения об ошибке'):
                alert_text = auth_page.get_text(auth_page.find_element(lloc.ALERT_LOGIN_ERROR))
                assert alert_text == exp_text['alert_text'], \
                    f'Текст ошибки не соответствует ожидаемому.'
