import allure
from data.locators.login_page_locators import LoginPageLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Авторизация')
@allure.feature('Страница авторизации')
@allure.story('Проверка фокуса поля ввода "Username" и скролла на странице')
@allure.severity(allure.severity_level.NORMAL)
def test_focus_and_scroll(pages):
    page = pages.login
    page.open(urls.LOGIN_PAGE)

    with allure.step('1. Установка фокуса в поле ввода "Username"'):
        page.set_focus(loc.USERNAME_FIELD)
        assert page.is_focused(loc.USERNAME_FIELD)

    with allure.step('2. Удаление фокуса из поля ввода "Username"'):
        page.del_focus()
        assert not page.is_focused(loc.USERNAME_FIELD)

    with allure.step('3. Проверка вертикального скролла'):
        assert not page.is_scroll('vertical')

    with allure.step('4. Проверка горизонтального скролла'):
        assert not page.is_scroll('horizontal')
