import allure

from data.locators.main_page_locators import NavigationLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Главная страница')
@allure.feature('Навигация')
@allure.story('Проверка перехода на другую страницу из меню навигации')
@allure.severity(allure.severity_level.NORMAL)
def test_following_from_navmenu(open_main_page, pages):
    main_page = open_main_page
    lifetime_page = pages.lifetime
    exp_text = lifetime_page.EXPECTED_TEXTS

    with allure.step('1. Нажать кнопку "All Courses" в меню навигации.'):
        main_page.click_element(loc.NAVI_ALL_COURSES_BUTTON)

    with allure.step('2. Кликнуть на пункт "Lifetime Membership".'):
        main_page.click_element(loc.LIFETIME_MENU_ITEM)

    with allure.step('3. Проверить текущий url, title страницы и heading-title.'):
        assert lifetime_page.get_current_url() == urls.LIFETIME_PAGE, 'Неверный url страницы'
        assert lifetime_page.get_title() == exp_text['lifetime_url_title'], 'Неверный title страницы'
