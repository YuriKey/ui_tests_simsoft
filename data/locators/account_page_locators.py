from selenium.webdriver.common.by import By


class AccountPage:
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[@ng-click='transactions()']")

    DEPOSIT_BUTTON = (By.XPATH, "//button[@ng-click='deposit()']")
    WITHDRAWL_BUTTON = (By.XPATH, "//button[@ng-click='withdrawl()']")
    AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    INFO_MESSAGE = (By.XPATH, "//span[@class='error ng-binding']")
    HELLO_MESSAGE = (By.XPATH, "//strong[contains(., 'Welcome')]")

    BALANCE_LOCATOR = (By.XPATH, "//div[@class='center']/strong[preceding-sibling::text()[1][contains(., 'Balance :')]]")



