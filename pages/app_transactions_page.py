from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.locators.transactions_page_locators import TransactionsPageLocators as loc

from pages.base_page import BasePage


class TransactionsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def get_all_transactions(self) -> list:
        wait = WebDriverWait(self.browser, 10)
        table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

        headers = table.find_elements(By.TAG_NAME, "th")
        header_texts = [header.text.strip().lower() for header in headers]

        date_index = header_texts.index("date-time") if "date-time" in header_texts else 0
        amount_index = header_texts.index("amount") if "amount" in header_texts else 1
        type_index = header_texts.index("transaction type") if "transaction type" in header_texts else 2

        rows = table.find_elements(By.TAG_NAME, "tr")[1:]

        transactions = []

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= max(date_index, amount_index, type_index) + 1:
                transaction = {
                    "date-time": cells[date_index].text.strip(),
                    "amount": int(cells[amount_index].text.strip()) if cells[amount_index].text.strip().isdigit() else
                    cells[amount_index].text.strip(),
                    "type": cells[type_index].text.strip().lower()
                }
                transactions.append(transaction)

        return transactions

    def find_transaction(self, amount, type_) -> bool:
        transactions = self.get_all_transactions()

        for transaction in transactions:
            if (transaction["amount"] == amount and
                    transaction["type"] == type_.lower()):
                return True

        return False

    def _get_credits_sum(self) -> int:
        all_transactions = self.get_all_transactions()
        total = 0
        for transaction in all_transactions:
            if transaction.get('type') == 'credit':
                total += transaction.get('amount', 0)
        return total

    def _get_debits_sum(self) -> int:
        all_transactions = self.get_all_transactions()
        total = 0
        for transaction in all_transactions:
            if transaction.get('type') == 'debit':
                total += transaction.get('amount', 0)
        return total

    def get_balance_by_table(self) -> int:
        try:
            balance = self._get_credits_sum() - self._get_debits_sum()
            return balance
        except Exception as e:
            raise Exception(f'Не удалось получить баланс из таблицы транзакций: {e}')

    def click_reset_button(self):
        try:
            self.click_element(loc.RESET_BUTTON)
        except Exception as e:
            raise Exception(f'Не удалось нажать кнопку сброса: {e}')

    def click_back_button(self):
        try:
            self.click_element(loc.BACK_BUTTON)
        except Exception as e:
            raise Exception(f'Не удалось нажать кнопку назад: {e}')
