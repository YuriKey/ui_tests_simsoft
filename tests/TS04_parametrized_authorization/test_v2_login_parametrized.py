import allure
import pytest

from data.locators.login_page_locators import LoginPageLocators as lloc
from data.urls import Urls
from pages.login_page import LoginPage as lp

urls = Urls()

TEST_CASES = lp.TEST_CASES


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Авторизация all type data')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('test_case',
                         TEST_CASES,
                         ids=[case['name'] for case in TEST_CASES])
def test_login_authorization(open_auth_page, pages, test_case):
    auth_page = open_auth_page
    home_page = pages.home
    exp_text = auth_page.EXPECTED_TEXTS

    with allure.step(f'Тестовый случай: {test_case['name']}'):
        with allure.step('1. Заполнить поля формы'):
            auth_page.fill_field(lloc.USERNAME_FIELD, test_case['credentials']['username'])
            auth_page.fill_field(lloc.PASSWORD_FIELD, test_case['credentials']['password'])
            auth_page.fill_field(lloc.USERNAME_DESC_FIELD, test_case['credentials']['username_desc'])

        with allure.step('2. Нажать  кнопку "Login"'):
            auth_page.click_element(lloc.LOGIN_BUTTON)

        if test_case['expected']['success']:
            home_page.await_for_js_reaction()
            with allure.step('3. Проверка URL страницы'):
                assert home_page.get_current_url() == test_case['expected']['url'], \
                    f'URL страницы не соответствует ожидаемому: {test_case['expected']['url']}'

            with allure.step('4. Проверка заголовка страницы'):
                assert home_page.get_title() == exp_text['page_title'], \
                    'Заголовок страницы не соответствует ожидаемому'

            with allure.step('5. Проверка текста сообщения'):
                assert home_page.get_text_by_locator(test_case['expected']['element']) == \
                        exp_text[test_case['expected']['text_key']], \
                        'Текст сообщения не соответствует ожидаемому'
        else:
            with allure.step('3. Проверка URL страницы'):
                assert auth_page.get_current_url() != urls.HOME_PAGE, \
                    'URL страницы изменился'
                with allure.step('4. Проверка наличия сообщения'):
                    assert auth_page.is_element_visible(test_case['expected']['element']), \
                        'Не отображается сообщение об ошибке'
                with allure.step('5. Проверка текста сообщения об ошибке'):
                    alert_text = auth_page.get_text(auth_page.find_element(test_case['expected']['element']))
                    assert alert_text == exp_text[test_case['expected']['text_key']], \
                        f'Текст ошибки не соответствует ожидаемому: {exp_text[test_case['expected']['text_key']]}'
