import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Элементы страниц')
@allure.feature('Взаимодействие с элементами страниц')
@allure.story('Переключение между вкладками')
@allure.severity(allure.severity_level.NORMAL)
def test_switch_tabs(pages):
    page = pages.tabs
    with allure.step('1. Открыть страницу упражнения'):
        page.open(urls.TABS_PAGE)

    with allure.step('2. Нажать на ссылку "New Browser Tab"'):
        page.switch_to_exerc_frame()
        page.open_new_tab()

    with allure.step('3. Перенести фокус на новую вкладку, нажать на ссылку "New Browser Tab"'):
        page.switch_to_some_tab(2)
        page.open_new_tab()

    with allure.step('4. Убедиться, что открылась третья вкладка'):
        page.switch_to_some_tab(3)
        current_tab_index = page.get_current_tab_index()
        assert current_tab_index == 3, \
            f'Текущая вкладка не 3, а {current_tab_index}'
