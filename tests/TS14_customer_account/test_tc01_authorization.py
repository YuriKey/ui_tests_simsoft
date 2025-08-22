import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт пользователя банка')
@allure.story('Авторизация пользователя')
@allure.severity(allure.severity_level.CRITICAL)
def test_user_authorization(pages, create_active_account):
    reg_page = pages.registration
    cust_page = pages.customer
    acc_page = pages.account
    user_data = create_active_account

    with allure.step('1. Переход в интерфейс "Customer Login"'):
        reg_page.click_customer_login()

    with allure.step('2. Выбор созданного покупателя'):
        cust_page.customer_select(f"{user_data['first_name']} {user_data['last_name']}")

    with allure.step('3. Нажатие кнопки "Login"'):
        cust_page.click_login_button()

    with allure.step('4. Проверка успешной авторизации'):
        expected_text = f"Welcome {user_data['first_name']} {user_data['last_name']} !!"
        actual_text = acc_page.get_welcome_message()
        assert expected_text == actual_text, \
            f"Текст приветствия: '{actual_text}' не соответствует ожидаемому: '{expected_text}'"
