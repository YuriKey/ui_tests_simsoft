import allure

from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Авторизация с невалидными данными')
@allure.severity(allure.severity_level.NORMAL)
def test_login_with_invalid_data(open_auth_page):
    auth_page = open_auth_page
    exp_text = auth_page.EXPECTED_TEXTS

    with allure.step('1. Ввести в поле "Username" значение "angula"'):
        auth_page.fill_field(loc.USERNAME_FIELD, 'angula'), \
            'Не удалось ввести в поле "Username" значение "angula"'

    with allure.step('2. Ввести в поле "Password" значение "password"'):
        auth_page.fill_field(loc.PASSWORD_FIELD, 'password'), \
            'Не удалось ввести в поле "Password" значение "password"'

    with allure.step('3. Ввести в поле "Username *" значение "angular"'):
        auth_page.fill_field(loc.USERNAME_DESC_FIELD, 'angular'), \
            'Не удалось ввести в поле "Username *" значение "angular"'

    with allure.step('4. Нажать кнопку "Login". '
                     'Проверить текущий url страницы, title страницы и надпись "You\'re logged in!!"'):
        auth_page.click_element(loc.LOGIN_BUTTON), \
            'Не удалось нажать кнопку "Login"'
        alert = auth_page.find_element(loc.ALERT_LOGIN_ERROR)

        assert auth_page.get_current_url() != urls.HOME_PAGE, 'URL страницы изменился'
        assert alert.is_displayed(), 'Не отображается сообщение об ошибке'
        assert alert.text == exp_text['alert_text'], 'Текст сообщения об ошибке не совпадает'
