import allure

from data.locators.main_page_locators import NavigationLocators as loc
from data.urls import Urls
from pages.main_page import MainPage as mp

urls = Urls()


@allure.epic("Главная страница")
@allure.feature("Навигация")
@allure.story("Проверка перехода на другую страницу из меню навигации")
@allure.severity(allure.severity_level.NORMAL)
def test_following_from_navmenu(open_main_page):
    page = open_main_page
    exp_text = mp.EXPECTED_TEXTS

    with allure.step("1. Нажать кнопку 'All Courses' в меню навигации."):
        page.click_element(loc.NAVI_ALL_COURSES_BUTTON)

    with allure.step("2. Кликнуть на пункт 'Lifetime Membership'."):
        page.click_element(loc.LIFETIME_MENU_ITEM)

    with allure.step("3. Проверить текущий url, title страницы и heading-title."):
        assert page.get_current_url() == urls.LIFETIME_PAGE, "Неверный url страницы"
        assert page.get_title() == exp_text["lifetime_url_title"], "Неверный title страницы"
