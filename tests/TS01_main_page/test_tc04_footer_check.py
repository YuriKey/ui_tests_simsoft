import allure

from data.locators.main_page_locators import FooterLocators as loc
from pages.main_page import MainPage as mp


@allure.epic('Главная страница')
@allure.feature('Элементы главной страницы')
@allure.story('Проверка контактной информации в футере')
@allure.severity(allure.severity_level.CRITICAL)
def test_header_contacts_check(open_main_page):
    page = open_main_page
    exp_text = mp.EXPECTED_TEXTS

    with allure.step('1. Проверить отображение адреса.'):
        elem = page.find_element(loc.ADDRESS)
        assert elem.text == exp_text['address'], 'Адрес не соответствует ожидаемому.'

    with allure.step('2. Проверить наличие номеров телефонов.'):
        num_1 = page.find_element(loc.PHONE1)
        num_2 = page.find_element(loc.PHONE2)
        assert num_1.text == exp_text['in_phone3'], 'Номер телефона не соответствует ожидаемому.'
        assert num_2.text == exp_text['in_phone4'], 'Номер телефона не соответствует ожидаемому.'

    with allure.step('3. Проверить отображение адресов email.'):
        addr_1 = page.find_element(loc.EMAIL1)
        addr_2 = page.find_element(loc.EMAIL2)
        assert addr_1.text == exp_text['mail'], 'Адрес электронной почты не соответствует ожидаемому.'
        assert addr_2.text == exp_text['mail2'], 'Адрес электронной почты не соответствует ожидаемому.'
