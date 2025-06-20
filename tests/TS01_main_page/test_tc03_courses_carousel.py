import allure

from data.locators.main_page_locators import CarouselLocators as loc


@allure.epic('Главная страница')
@allure.feature('Элементы главной страницы')
@allure.story('Проверка блока с курсами')
@allure.severity(allure.severity_level.NORMAL)
def test_courses_carousel(open_main_page):
    main_page = open_main_page

    with allure.step('1. Проверка блока с курсами и кнопок навигации блока'):
        main_page.scroll_to_element(loc.COURSES_BLOCK)

        assert main_page.is_element_visible(loc.COURSES_BLOCK), 'Блок с курсами не найден'
        assert main_page.is_element_visible(loc.BTN_LEFT), 'Кнопка "Влево" не найдена'
        assert main_page.is_element_visible(loc.BTN_RIGHT), 'Кнопка "Вправо" не найдена'

    main_page.next_slide()
    main_page.close_banner()
    first_slide_label = main_page.get_active_slide_label()

    with allure.step('2. Нажать кнопку "Вправо"'):
        main_page.next_slide()
        second_slide_label = main_page.get_active_slide_label()

        assert second_slide_label != first_slide_label, 'Слайд не сменился'

    with allure.step('3. Нажать дважды кнопку "Влево"'):
        main_page.previous_slide()
        main_page.previous_slide()
        third_slide_label = main_page.get_active_slide_label()

        assert third_slide_label != second_slide_label, 'Слайд не сменился'
