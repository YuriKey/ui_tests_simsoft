import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт пользователя банка')
@allure.story('Проверка корректности подсчета баланса')
@allure.severity(allure.severity_level.NORMAL)
def test_check_balance(pages, login_new_user_with_history):
    acc_page = pages.account
    tr_page = pages.transactions

    with allure.step('1. Получение состояния баланса'):
        row_balance = acc_page.get_balance_by_info_row()
        assert row_balance > 0, \
            f'Баланс пользователя {login_new_user_with_history} должен быть больше нуля'

    with allure.step('2. Переход на вкладку "Transactions"'):
        acc_page.click_transactions_button()
        assert tr_page.get_current_url() == urls.APP_TRANSACTIONS_PAGE, \
            f'Не удалось перейти на страницу "Transactions"'

    with allure.step('3. Подсчет баланса из таблицы транзакций'):
        table_balance = tr_page.get_balance_by_table()

    with allure.step('4. Проверка данных'):
        assert row_balance == table_balance, \
            f'Данные таблицы и строки не совпадают: {row_balance} != {table_balance}'
