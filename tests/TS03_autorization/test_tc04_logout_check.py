import allure

from data.locators.home_page_locators import HomePageLocators as hloc
from data.locators.login_page_locators import LoginPageLocators as lploc
from data.urls import Urls

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Проверка кнопки Logout')
@allure.severity(allure.severity_level.CRITICAL)
def test_logout_check(login, pages):
    home_page = login
    login_page = pages.login
    with allure.step('1. Проверить текущую страницу пользователя'):
        assert home_page.get_current_url() == urls.HOME_PAGE, 'URL страницы некорректен.'

    with allure.step('2. Нажать кнопку Logout'):
        logout = home_page.find_element(hloc.LOGOUT_BUTTON)
        home_page.click_element_by_js(logout)

    with allure.step('3. Проверить текущую страницу'):
        assert login_page.get_current_url() == urls.LOGIN_PAGE, 'URL страницы некорректен.'

    with allure.step('4. Проверить наличие полей "Username" и "Password"'):
        username_field = login_page.find_element(lploc.USERNAME_FIELD)
        password_field = login_page.find_element(lploc.PASSWORD_FIELD)
        assert username_field, 'Поле "Username" не отображается'
        assert password_field, 'Поле "Password" не отображается'
