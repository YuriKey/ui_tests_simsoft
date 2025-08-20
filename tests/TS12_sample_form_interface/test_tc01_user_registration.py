import allure

from data.locators.registration_page_locators import RegistrationPageLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Форма авторизации')
@allure.story('Регистрация нового пользователя')
@allure.severity(allure.severity_level.CRITICAL)
def test_user_registration(pages):
    reg_page = pages.registration
    exp_text = reg_page.EXPECTED_TEXTS

    with allure.step('1. проверка открытия интерфейса Sample Form'):
        reg_page.open(urls.APP_LOGIN_PAGE)
        reg_page.click_element(loc.REGISTER_BUTTON)
        assert reg_page.get_current_url() == urls.APP_REG_PAGE, \
            'Неверный URL страницы регистрации'
        assert reg_page.get_title() == exp_text['page_title'], \
            'Неверный заголовок страницы регистрации'

    with allure.step('2. Заполнение формы регистрации корректными данными'):
        reg_page.fill_complete_registration_form()

    with allure.step('3. Нажатие кнопки Register'):
        reg_page.click_register_button()

    with allure.step('4. Проверка сообщение об успешной регистрации'):
        assert reg_page.verify_success_message(), \
            'Сообщение об успешной регистрации не отображается'
