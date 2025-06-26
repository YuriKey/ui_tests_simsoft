import os

import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Авторизация на httpwatch')
@allure.story('Авторизация с валидными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_basic_auth(pages):
    page = pages.basic_auth

    with allure.step('1. Открыть страницу авторизации httpwatch'):
        page.open(urls.BASIC_AUTH_PAGE)

    with allure.step('2. Нажать на кнопку "Display Image"'):
        page.click_display_image()

    with allure.step('3. Пройти авторизацию'):
        page.fill_fields_and_accept()

    with allure.step('4. Проверить, что авторизация прошла успешно'):
        assert page.is_image_displayed()
        credentials = page.get_credentials_from_image()
        assert credentials['username'] == os.getenv('WATCH_LOGIN')
        assert credentials['password'] == os.getenv('WATCH_PASSWORD')
