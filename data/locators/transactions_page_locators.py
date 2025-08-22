from selenium.webdriver.common.by import By


class TransactionsPageLocators:
    BACK_BUTTON = (By.XPATH, "//button[@ng-click='back()']")
    RESET_BUTTON = (By.XPATH, "//button[@ng-click='reset()']")