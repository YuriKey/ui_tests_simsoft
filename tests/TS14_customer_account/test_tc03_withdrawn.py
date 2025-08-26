import allure
import pytest

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт пользователя банка')
@allure.story('Частичное снятие денег со счета')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    'amount, expected_text, type_', [
        (pytest.param('random', 'Transaction successful', 'debit')),
        (0, '', 'debit'),
        (-100322, '', 'debit'),
        (1000000, 'Transaction Failed. You can not withdraw amount more than the balance.', 'debit')
    ]
)
def test_withdraw(pages, login_new_user_with_notnull_balance, amount, expected_text, type_):
    acc_page = pages.account
    tr_page = pages.transactions

    with allure.step('1. Проверка баланса'):
        balance = acc_page.get_balance_by_info_row()
        assert balance == 100321, \
            f'Не корректный баланс. Ожидалось: 100321, получено: {balance}'

    with allure.step('2. Нажатие кнопки "Withdrawl"'):
        acc_page.click_withdrawl_button()

    with allure.step('3. Ввод суммы'):
        if amount == 'random':
            actual_amount = acc_page.get_random_deposit_amount(balance)
        else:
            actual_amount = amount
        acc_page.fill_amount_field(actual_amount)

    with allure.step('4. Нажатие на кнопку подтверждения "Withdrawn"'):
        acc_page.click_submit_button()

    with allure.step('5. Проверка сообщения'):
        assert acc_page.get_operation_message() == expected_text, \
            f"Текст сообщения не соответствует ожидаемому. Ожидаемый текст: {expected_text}, " \
            f"полученный текст: {acc_page.get_operation_message()}"

    with allure.step('6. Переход на вкладку "Transactions"'):
        acc_page.click_transactions_button()

    with allure.step(f'7. Проверка наличия транзакции на {actual_amount}'):
        transaction_found = tr_page.find_transaction(amount=actual_amount, type_=type_)
        if amount == 'random':
            assert transaction_found, f"Транзакция с amount={actual_amount} не найдена"
        else:
            assert not transaction_found, f"Неожиданно найдена транзакция для amount={amount}"
