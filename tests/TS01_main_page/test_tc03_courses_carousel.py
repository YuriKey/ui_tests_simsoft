import time

import allure
import pytest

from data.locators.main_page_locators import CarouselLocators as loc


@allure.epic('Главная страница')
@allure.feature('Элементы главной страницы')
@allure.story('Проверка блока с курсами')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(reason='unknown reason')
def test_courses_carousel(open_main_page):
    page = open_main_page
    courses_block = page.find_element(loc.COURSES_BLOCK)
    previous_button = page.find_element(loc.BTN_LEFT)
    next_button = page.find_element(loc.BTN_RIGHT)

    with allure.step('1. Проверка блока с курсами и кнопок навигации блока'):
        page.scroll_to_element(loc.COURSES_BLOCK)
        assert courses_block.is_displayed(), 'Блок с курсами не найден'
        assert previous_button.is_displayed(), 'Кнопка "Влево" не найдена'
        assert next_button.is_displayed(), 'Кнопка "Вправо" не найдена'

    page.click_element_by_js(next_button)
    page.close_banner()
    first_slide_label = page.get_active_slide_label()

    with allure.step('2. Нажать кнопку "Вправо"'):
        page.click_element_by_js(next_button)
        second_slide_label = page.get_active_slide_label()
        assert second_slide_label != first_slide_label, 'Слайд не сменился'

    with allure.step('3. Нажать дважды кнопку "Влево"'):
        page.click_element_by_js(previous_button)
        time.sleep(1)
        page.click_element_by_js(previous_button)
        third_slide_label = page.get_active_slide_label()
        assert third_slide_label != second_slide_label, 'Слайд не сменился'
