import allure
import pytest

from data.urls import Urls

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации на sqlex')
@allure.story('Авторизация с использованием cookies')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup")
def test_auth_with_cookies(pages):
    sqlex_page = pages.sqlex.open_page()
    sqlex_page.load_cookies_and_refresh()

    if not sqlex_page.is_logged_in():
        sqlex_page.sqlex_login()
        assert sqlex_page.is_logged_in(), "Авторизация не удалась"
    else:
        assert True
