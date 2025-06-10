# test_tc01_open_main_page.py

import allure

from data.locators.main_page_locators import MainPageLocators as loc
from data.urls import Urls
from pages.main_page import MainPage as mp

urls = Urls()


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка открытия главной страницы")
@allure.severity(allure.severity_level.BLOCKER)
def test_main_page_open(browser):
    page = mp(browser)
    page.open(urls.MAIN_PAGE)
    exp_text = mp.EXPECTED_TEXTS

    with allure.step("1. Проверка текущего URL и заголовка страницы"):
        assert page.get_current_url() == urls.MAIN_PAGE, "Неверный URL главной страницы"
        assert page.get_title() == exp_text["url_title"], "Неверный заголовок страницы"

    with allure.step("2. Проверка наличия и текста кнопок в блоке навигации"):
        navigation_elements = loc.NAVIGATION_ELEMENTS
        missing_elements = mp.check_elements_with_text(navigation_elements, page)

        assert not missing_elements, (f"Отсутствуют следующие элементы навигации:"
                                      f" {', '.join(missing_elements)}")

    with allure.step("3. Проверка наличия и текста кнопки регистрации"):
        reg_button = page.find_element(loc.REGISTER_BUTTON)

        assert reg_button, "Кнопка регистрация отсутствует"
        assert reg_button.text == exp_text["reg_button_text"], "Неверный текст для кнопки регистрация"

    with allure.step("4. Проверка наличия и текста блока курсов"):
        block_element = page.find_element(loc.COURSES_BLOCK_CONTAINER)

        assert exp_text["block_courses_title"] in block_element.text, "Блок курсов не содержит заголовок"
        assert exp_text["life_time_text"] in block_element.text, "Блок курсов не содержит Lifetime Membership"
        assert exp_text["training_text"] in block_element.text, "Блок курсов не содержит Online Training"
        assert exp_text["tutorials_text"] in block_element.text, "Блок курсов не содержит Video Tutorials"
        assert exp_text["corporate_text"] in block_element.text, "Блок курсов не содержит Corporate Training"

