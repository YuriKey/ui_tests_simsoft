import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт менеджера банка')
@allure.story('Чтение пользователя')
@allure.severity(allure.severity_level.NORMAL)
def test_read_customer(pages, create_user):
    man_page = pages.manager
    read_page = pages.read_user
    user_data = create_user
    man_page.open(urls.APP_LOGIN_PAGE)
    man_page.click_manager_login_button()
    exp_text = read_page.EXPECTED_TEXTS
    man_page.open_account_button()

    with allure.step("1. Выбор созданного аккаунта"):
        read_page.fill_customer_name(user_data['first_name'])

    with allure.step("2. Выбор валюты"):
        read_page.fill_currency()

    with allure.step("3. Нажатие кнопки 'Process'"):
        read_page.click_process_button()

    with allure.step("4. Проверка появления всплывающего окна"):
        alert = man_page.switch_to_alert()
        actual_text = alert.text
        man_page.accept_alert()
        assert actual_text.startswith(exp_text['alert_text']), \
            'Неверный текст всплывающего окна'
