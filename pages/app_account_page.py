import random

import allure

from data.locators.account_page_locators import AccountPage as loc
from pages.base_page import BasePage


class AccountPage(BasePage):
    EXPECTED_TEXT = {
        "deposit_massege": "Deposit Successful",
        "withdrawl_message": "Transaction successful",
    }

    def __init__(self, browser):
        super().__init__(browser)

    def click_deposit_button(self) -> None:
        with allure.step("Клик на кнопку депозита"):
            try:
                self.click_element(loc.DEPOSIT_BUTTON)
                self.await_for_js_reaction()
            except Exception as e:
                raise Exception(f"Не удалось кликнуть на кнопку вкладки депозита: {e}")

    def click_withdrawl_button(self) -> None:
        with allure.step("Клик на кнопку вкладки Withdrawl"):
            try:
                self.click_element(loc.WITHDRAWL_BUTTON)
                self.await_for_js_reaction()
            except Exception as e:
                raise Exception(f"Не удалось кликнуть на кнопку вкладки Withdrawl: {e}")

    def click_transactions_button(self) -> None:
        with allure.step("Клик на кнопку вкладки транзакций"):
            try:
                self.click_element(loc.TRANSACTIONS_BUTTON)
                self.await_for_js_reaction()
            except Exception as e:
                raise Exception(f"Не удалось кликнуть на кнопку вкладки транзакций: {e}")

    def get_balance_by_info_row(self) -> int:
        with allure.step("Получение баланса из строки информации"):
            try:
                balance_element = self.find_element(loc.BALANCE_LOCATOR)
                return int(balance_element.text.strip())
            except Exception as e:
                raise Exception(f"Не удалось получить баланс из строки информации: {e}")

    def fill_amount_field(self, amount) -> None:
        with allure.step("Заполнение поля суммы"):
            try:
                self.fill_field(loc.AMOUNT_FIELD, amount)
            except Exception as e:
                raise Exception(f"Не удалось заполнить поле суммы: {e}")

    def click_submit_button(self) -> None:
        with allure.step("Клик на кнопку подтверждения"):
            try:
                self.click_element(loc.SUBMIT_BUTTON)
                self.await_for_js_reaction()
            except Exception as e:
                raise Exception(f"Не удалось кликнуть на кнопку подтверждения: {e}")

    def get_welcome_message(self) -> str:
        with allure.step("Получение приветственного сообщения"):
            try:
                welcome_element = self.find_element(loc.HELLO_MESSAGE)
                return welcome_element.text.strip()
            except Exception as e:
                raise Exception(f"Не удалось получить приветственное сообщение: {e}")

    def get_operation_message(self) -> str:
        with allure.step("Получение текста сообщения об успешном депозите"):
            try:
                element = self.find_element(loc.INFO_MESSAGE)
                return element.text
            except Exception:
                return ""

    @staticmethod
    def get_random_deposit_amount(current_balance) -> int:
        with allure.step("Генерация случайного депозита"):
            if current_balance <= 0:
                return 0

            return random.randint(0, current_balance)
