import allure
from data.locators.login_page_locators import LoginPageLocators as loc
from data.locators.home_page_locators import HomePageLocators as hloc
from data.urls import Urls

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Авторизация с валидными данными')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_valid_data(open_auth_page, pages):
    auth_page = open_auth_page
    home_page = pages.login
    exp_text = auth_page.EXPECTED_TEXTS

    with allure.step('1. Ввести в поле "Username" значение "angular"'):
        auth_page.fill_field(loc.USERNAME_FIELD, 'angular'), \
            'Не удалось ввести в поле "Username" значение "angular"'

    with allure.step('2. Ввести в поле "Password" значение "password"'):
        auth_page.fill_field(loc.PASSWORD_FIELD, 'password'), \
            'Не удалось ввести в поле "Password" значение "password"'

    with allure.step('3. Ввести в поле "Username *" значение "angular"'):
        auth_page.fill_field(loc.USERNAME_DESC_FIELD, 'angular'), \
            'Не удалось ввести в поле "Username *" значение "angular"'

    with allure.step('4. Нажать кнопку "Login". '
                     'Проверить текущий url страницы, title страницы и надпись "You\'re logged in!!"'):
        auth_page.click_element(loc.LOGIN_BUTTON), 'Не удалось нажать кнопку "Login"'

        assert home_page.get_text_by_locator(hloc.SUCCESS_MESSAGE) == exp_text['success_text'], \
            'Некорректный текст на "Home Page"'
        assert home_page.get_current_url() == urls.HOME_PAGE, \
            'Не корректный url страницы "Home Page"'
        assert home_page.get_title() == exp_text['page_title'], \
            'некорректный title страницы "Home Page"'
