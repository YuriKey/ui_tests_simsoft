from selenium.webdriver.common.by import By


class ReadUserPageLocators:
    USER_SELECT = (By.XPATH, "//select[@name='userSelect']")
    CURRENCY_SELECT = (By.XPATH, "//select[@name='currency']")
    PROCESS_BUTTON = (By.XPATH, "//button[@type='submit']")

    TEST_USER_LOCATOR = (By.XPATH, "//*[contains(text(), 'Test User')]")
