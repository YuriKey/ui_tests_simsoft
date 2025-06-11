import allure

from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls
from pages.login_page import LoginPage as lp

urls = Urls()


@allure.epic("Авторизация")
@allure.feature("Страница авторизации")
@allure.story("Проверка наличия полей ввода")
@allure.severity(allure.severity_level.CRITICAL)
def test_check_input_fields(browser):
    page = lp(browser)
    exp_text = lp.EXPECTED_TEXTS

    with allure.step("1. Открытие страницы авторизации"):
        page.open(urls.LOGIN_PAGE)
        assert page.get_current_url() == urls.LOGIN_PAGE, "URL не соответствует ожидаемому"
        assert page.get_title() == exp_text["page_title"], "Заголовок страницы не соответствует ожидаемому"

    with allure.step("2. Проверка наличия поля username"):
        username_field = page.find_element(loc.USERNAME_FIELD)
        assert username_field, "Поле 'Username' не отображается"

    with allure.step("3. Проверка наличия поля password"):
        password_field = page.find_element(loc.PASSWORD_FIELD)
        assert password_field, "Поле 'Password' не отображается"

    with allure.step("4. Проверка отображения кнопки 'Login'"):
        login_button = page.find_element(loc.LOGIN_BUTTON)
        assert login_button, "Кнопка 'Login' не отображается"
        assert login_button.get_attribute("disabled"), "Кнопка 'Login'активна"
        assert login_button.value_of_css_property("cursor") == exp_text["not_cursor"], "Кнопка 'Login' активна"
