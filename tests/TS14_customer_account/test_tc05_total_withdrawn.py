import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт пользователя банка')
@allure.story('Полное снятие средств')
@allure.severity(allure.severity_level.CRITICAL)
def test_total_withdrawn(pages, login_new_user_with_notnull_balance):
    acc_page = pages.account
    exp_text = acc_page.EXPECTED_TEXT

    with allure.step('1. Получение баланса'):
        current_balance = acc_page.get_balance_by_info_row()
        assert current_balance >= 0, \
            'Баланс не может быть отрицательным'

    with allure.step('2. Нажатие кнопки "Withdrawn"'):
        acc_page.click_withdrawl_button()

    with allure.step('3. Ввод суммы, равной балансу'):
        acc_page.fill_amount_field(current_balance)

    with allure.step('4. Нажатие кнопки "Withdrawn"'):
        acc_page.click_submit_button()

    with allure.step('5. Проверка сообщения об успешном переводе'):
        actual_text = acc_page.get_operation_message()
        assert exp_text['withdrawl_message'] == actual_text, \
            f'Текст сообщения об успешном переводе не совпадает с ожидаемым. ' \
            f'Ожидалось: {exp_text["withdrawl_message"]}. ' \
            f'Получено: {actual_text}.'

    with allure.step('6. Проверка, что баланс равен нулю'):
        current_balance = acc_page.get_balance_by_info_row()
        assert current_balance == 0, \
            'Баланс не равен нулю.'
