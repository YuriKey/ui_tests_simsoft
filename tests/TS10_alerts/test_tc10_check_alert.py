import allure

from data.locators.alerts_locators import AlertsLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Элементы страниц')
@allure.feature('Взаимодействие с элементами страниц')
@allure.story('Взаимодействие с алертами')
@allure.severity(allure.severity_level.NORMAL)
def test_check_alert(pages):
    page = pages.alerts
    exp_text = page.EXPECTED_TEXT['result_text']

    with allure.step('1. Открыть страницу упражнения'):
        page.open(urls.ALERTS_PAGE)

    with allure.step('2. Нажать кнопку "Input Alert"'):
        page.press_input_alert()

    with allure.step('3. Нажать кнопку вызова алерта. Ввести кастомный текст и подтвердить'):
        page.trigger_alert()
        page.input_text_and_submit()

    with allure.step('4. Проверить, что текст применился'):
        act_text = page.get_text_by_locator(loc.RESULT_MESSAGE)
        assert exp_text == act_text, \
            'Ожидаемый и фактический тексты не совпадают'
