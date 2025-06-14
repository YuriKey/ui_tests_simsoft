import allure

from data.urls import Urls
from utils.decorators import screenshot_on_failure

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Проверка открытия страницы авторизации')
@allure.severity(allure.severity_level.CRITICAL)
@screenshot_on_failure
def test_open_login_page(pages):
    login_page = pages.login
    exp_text = login_page.EXPECTED_TEXTS

    with allure.step('1. Открытие страницы авторизации'):
        login_page.open(urls.LOGIN_PAGE)

    with allure.step('2. Проверка заголовка страницы'):
        assert login_page.get_current_url() == urls.LOGIN_PAGE, \
            f'Ожидался URL: {urls.WRONG_LOGIN_PAGE}'

    with allure.step('3. Проверка заголовка страницы'):
        assert login_page.get_title() == exp_text['wrong_page_title'], \
            f'Ожидался заголовок: {exp_text['wrong_page_title']}'
