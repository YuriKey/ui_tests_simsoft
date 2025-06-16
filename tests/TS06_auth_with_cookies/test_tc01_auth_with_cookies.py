import allure

from utils.cookies_helper import CookiesHelper as ch


@allure.epic('Авторизация')
@allure.feature('Страница авторизации на sqlex')
@allure.story('Авторизация с использованием cookies')
@allure.severity(allure.severity_level.NORMAL)
def test_auth_via_cookies(pages, prepare_auth_cookies):
    with allure.step("1. Открыть страницу"):
        sqlex_page = pages.sqlex.open_page()

    with allure.step("2. Загрузить сохраненные cookies и обновить страницу"):
        cookies_helper = ch(sqlex_page, prepare_auth_cookies)
        cookies_helper.load_cookies_and_refresh()

    with allure.step("3. Проверить успешную авторизацию"):
        assert sqlex_page.is_logged_in(), \
            "Пользователь не авторизован после загрузки cookies"
