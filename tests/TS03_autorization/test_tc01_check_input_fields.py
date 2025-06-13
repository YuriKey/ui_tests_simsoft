import allure

from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Проверка наличия полей ввода')
@allure.severity(allure.severity_level.CRITICAL)
def test_check_input_fields(pages):
    login_page = pages.login
    exp_text = login_page.EXPECTED_TEXTS

    with allure.step('1. Открытие страницы авторизации'):
        login_page.open(urls.LOGIN_PAGE)

        assert login_page.get_current_url() == urls.LOGIN_PAGE, \
            f'Ожидался URL: {urls.LOGIN_PAGE}'
        assert login_page.get_title() == exp_text['page_title'], \
            f'Ожидался заголовок: {exp_text['page_title']}'

    with allure.step('2. Проверка наличия поля username'):
        username_field = login_page.find_element(loc.USERNAME_FIELD)
        username_label = login_page.get_field_label(loc.USERNAME_FIELD)

        assert username_field, 'Поле "Username" не отображается'
        assert username_label == exp_text['username_label'], \
            'Некорректное название поля "Username"'

    with allure.step('3. Проверка наличия поля password'):
        password_field = login_page.find_element(loc.PASSWORD_FIELD)
        password_label = login_page.get_field_label(loc.PASSWORD_FIELD)

        assert password_field, 'Поле "Password" не отображается'
        assert password_label == exp_text['password_label'], \
            'Некорректное название поля "Password"'

    with allure.step('4. Проверка отображения кнопки "Login"'):
        login_button = login_page.find_element(loc.LOGIN_BUTTON)

        assert login_button, 'Кнопка "Login" не отображается'
        assert login_page.get_attribute_(login_button, 'disabled'), \
            'Кнопка "Login" активна'
        assert login_page.get_prop_value(login_button, 'cursor') == exp_text['not_cursor'], \
               'Кнопка "Login" активна'
        assert login_page.get_text(login_button) == exp_text['login_button'], \
            'Некорректный текст кнопки "Login"'
