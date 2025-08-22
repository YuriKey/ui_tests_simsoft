import allure
import pytest

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт пользователя банка')
@allure.story('Пополнение счета')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    'amount, expected_text, type_', [
        (100321, 'Deposit Successful', 'credit'),
        (0, '', 'credit'),
        (-100322, '', 'credit')
    ]
)
def test_deposit(pages, login_new_user, amount, expected_text, type_):
    acc_page = pages.account
    tr_page = pages.transactions

    with allure.step('1. Переход на вкладку "Deposite"'):
        acc_page.click_deposit_button()

    with allure.step(f'2. Ввод суммы {amount}'):
        acc_page.fill_amount_field(amount=amount)

    with allure.step('3. Нажатие кнопки "Deposit"'):
        acc_page.click_submit_button()

    with allure.step('4. Проверка сообщения'):
        assert acc_page.get_operation_message() == expected_text, \
            f"Текст сообщения не соответствует ожидаемому. Ожидаемый текст: {expected_text}, " \
            f"полученный текст: {acc_page.get_operation_message()}"

    with allure.step('5. Переход на вкладку "Transactions"'):
        acc_page.click_transactions_button()

    with allure.step(f'6. Проверка наличия пополнения на {amount}'):
        transaction_found = tr_page.find_transaction(amount=amount, type_=type_)

        if amount > 0:
            assert transaction_found, \
                f"Транзакция с amount={amount} и type='credit' не найдена. " \
                f"Все транзакции: {tr_page.get_all_transactions()}"
        else:
            assert not transaction_found, \
                f"Неожиданно найдена транзакция для amount={amount}"
