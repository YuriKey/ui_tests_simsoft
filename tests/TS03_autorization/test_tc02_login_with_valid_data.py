import allure

from data.locators.login_page_locators import LoginPageLocators as loc
from data.locators.home_page_locators import HomePageLocators as hloc
from data.urls import Urls
from pages.login_page import LoginPage as lp

urls = Urls()


@allure.epic("Авторизация")
@allure.feature("Страница авторизации")
@allure.story("Авторизация с валидными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_valid_data(open_auth_page):
    page = open_auth_page
    exp_text = lp.EXPECTED_TEXTS

    with allure.step("1. Ввести в поле 'Username' значение 'angular'"):
        page.fill_field(loc.USERNAME_FIELD, "angular"), "Не удалось ввести в поле 'Username' значение 'angular'"

    with allure.step("2. Ввести в поле 'Password' значение 'password'"):
        page.fill_field(loc.PASSWORD_FIELD, "password"), "Не удалось ввести в поле 'Password' значение 'password'"

    with allure.step("3. Ввести в поле 'Username *' значение 'angular'"):
        page.fill_field(loc.USERNAME_DESC_FIELD, "angular"), "Не удалось ввести в поле 'Username *' значение 'angular'"

    with allure.step("4. Нажать кнопку 'Login'. "
                     "Проверить текущий url страницы, title страницы и надпись 'You're logged in!!'"):
        page.click_element(loc.LOGIN_BUTTON), "Не удалось нажать кнопку 'Login'"
        assert page.find_element(hloc.SUCCESS_MESSAGE).text == exp_text["success_text"], "Некорректный текст на 'Home Page'"
        assert page.get_current_url() == urls.HOME_PAGE, "Не корректный url страницы 'Home Page'"
        assert page.get_title() == exp_text["page_title"], "некорректный title страницы 'Home Page'"
