import allure
from data.locators.droppable_locators import DndLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Элементы страниц')
@allure.feature('Взаимодействие с элементами страниц')
@allure.story('Drag and Drop')
@allure.severity(allure.severity_level.NORMAL)
def test_dragndrop(pages):
    page = pages.dragndrop
    exp_text = page.EXPECTED_TEXTS

    with allure.step('1. Открыть страницу Drag and Drop'):
        page.open(urls.DND_PAGE)
        page.switch_to_dnd_frame()

    with allure.step('2. Сохранить текст принимающего фрейма до перетаскивания'):
        text_before = page.get_text_by_locator(loc.TEXT_BEFORE)

    with allure.step('3. Перетащить элемент drag на элемент drop'):
        page.drag_and_drop(loc.DRAGGABLE, loc.DROPPABLE)

    with allure.step('4. Сохранить текст принимающего фрейма после перетаскивания'):
        text_after = page.get_text_by_locator(loc.TEXT_AFTER)

    with allure.step('5. Сравнить ожидаемые и фактические тексты'):
        assert exp_text['text_before'] == text_before, \
            (f'Текст до перетаскивания не совпадает с ожидаемым. '
             f'Ожидаемый: {exp_text['text_before']}, получен: {text_before}')
        assert exp_text['text_after'] == text_after, \
            (f'Текст после перетаскивания не совпадает с ожидаемым.'
             f'Ожидаемый: {exp_text['text_after']}, получен: {text_after}')




