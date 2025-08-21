import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт менеджера банка')
@allure.story('Чтение пользователя')
@allure.severity(allure.severity_level.NORMAL)
def test_read_customer(pages):
    man_page = pages.manager
    read_page = pages.read_user
    man_page.open(urls.APP_LOGIN_PAGE)
    exp_text = read_page.EXPECTED_TEXTS
    man_page.create_new_customer()
    man_page.open_account_button()

    with allure.step("1. Выбор созданного аккаунта"):
        try:
            read_page.fill_customer_name()
        except Exception as e:
            raise Exception(f"Не удалось выбрать созданный аккаунт: {e}")

    with allure.step("2. Выбор валюты"):
        try:
            read_page.fill_currency()
        except Exception as e:
            raise Exception(f"Не удалось выбрать валюту: {e}")

    with allure.step("3. Нажатие кнопки 'Process'"):
        try:
            read_page.process_button_click()
        except Exception as e:
            raise Exception(f"Не удалось нажать кнопку 'Process': {e}")

    with allure.step("4. Проверка появления всплывающего окна"):
        alert = man_page.switch_to_alert()
        actual_text = alert.text
        man_page.accept_alert()
        assert actual_text.startswith(exp_text['alert_text']), \
            'Неверный текст всплывающего окна'
