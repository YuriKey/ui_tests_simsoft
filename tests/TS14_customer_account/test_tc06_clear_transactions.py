import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт пользователя банка')
@allure.story('Проверка очистки истории транзакций')
@allure.severity(allure.severity_level.NORMAL)
def test_clear_transactions(pages, login_new_user_with_history):
    acc_page = pages.account
    tr_page = pages.transactions

    with allure.step('Шаг 1. Нажатие кнопки "Transactions"'):
        acc_page.click_transactions_button()

    with allure.step('Шаг 2. Получение количества транзакций'):
        expected_transactions_count = len(tr_page.get_all_transactions())

    with allure.step('Шаг 3. Нажатие кнопки "Reset")'):
        tr_page.click_reset_button()

    with allure.step('Шаг 4. Проверка наличия транзакций'):
        actual_transactions_count = len(tr_page.get_all_transactions())
        assert expected_transactions_count != actual_transactions_count, \
            f'Количество транзакций совпадает. Ожидаемое количество: {expected_transactions_count}, ' \
            f'Фактическое - тоже: {actual_transactions_count}'
        assert actual_transactions_count == 0, \
            f'Количество транзакций не равно 0. Ожидаемое: 0, Фактическое: {actual_transactions_count}'

    with allure.step('Шаг 5. Нажатие кнопки "Back"'):
        tr_page.click_back_button()

    with allure.step('Шаг 6. Проверка текущего баланса'):
        current_balance = acc_page.get_balance_by_info_row()
        assert current_balance == 0, \
            f'Баланс не равен 0. Ожидаемое: 0, Фактическое: {current_balance}'
