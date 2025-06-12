import allure

from data.locators.main_page_locators import HeaderLocators as loc


@allure.epic('Главная страница')
@allure.feature('Навигация')
@allure.story('Проверка отображения меню навигации при скроллинге')
@allure.severity(allure.severity_level.NORMAL)
def test_check_navmenu_after_scroll(open_main_page):
    main_page = open_main_page

    with allure.step('1. Проскроллить страницу до конца'):
        main_page.scroll_to_bottom()

    with allure.step('2. Проверить отображение меню навигации'):
        assert main_page.element_is_visible(loc.HEADER)
